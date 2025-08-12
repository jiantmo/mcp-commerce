# Remove hardcoded fallback URLs from all controllers
Write-Host "Removing hardcoded fallback URLs from all controllers..."

# Get all controller files 
$controllers = Get-ChildItem "c:\github\mcp-commerce\mcp_dynamics365_commerce_server\controllers\*.py" | Where-Object { 
    $_.Name -ne "__init__.py" 
}

foreach ($controller in $controllers) {
    $content = Get-Content $controller.FullName -Raw
    $updated = $false
    
    Write-Host "  Processing $($controller.Name)..."
    
    # Replace hardcoded fallback URLs in handle_tool methods
    $patterns = @(
        'arguments\.get\("baseUrl",\s*"https://sculxdon4av67499847-rs\.su\.retail\.test\.dynamics\.com"\)',
        'arguments\.get\(''baseUrl'',\s*''https://sculxdon4av67499847-rs\.su\.retail\.test\.dynamics\.com''\)',
        'arguments\.get\("baseUrl",\s*"https://your-commerce-site\.com"\)',
        'arguments\.get\(''baseUrl'',\s*''https://your-commerce-site\.com''\)'
    )
    
    foreach ($pattern in $patterns) {
        if ($content -match $pattern) {
            $content = $content -replace $pattern, 'arguments.get("baseUrl", get_base_url())'
            $updated = $true
        }
    }
    
    # Save the file if it was updated
    if ($updated) {
        $content | Set-Content $controller.FullName -NoNewline
        Write-Host "    ✓ Removed hardcoded fallback URL from $($controller.Name)"
    } else {
        Write-Host "    - No hardcoded fallback URLs found in $($controller.Name)"
    }
}

Write-Host "`nCompleted! All controllers now use get_base_url() as fallback instead of hardcoded URLs."
