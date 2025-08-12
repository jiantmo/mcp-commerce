# Update all controllers to use centralized base URL configuration
Write-Host "Updating all controllers to use centralized base URL configuration..."

# Get all controller files that need updating
$controllers = Get-ChildItem "c:\github\mcp-commerce\mcp_dynamics365_commerce_server\controllers\*.py" | Where-Object { 
    $_.Name -ne "__init__.py" -and $_.Name -ne "base_controller.py" 
}

foreach ($controller in $controllers) {
    $content = Get-Content $controller.FullName -Raw
    $updated = $false
    
    # Skip files that already import get_base_url
    if ($content -match "from \.\.config import get_base_url") {
        Write-Host "  $($controller.Name) already uses centralized config - skipping"
        continue
    }
    
    Write-Host "  Processing $($controller.Name)..."
    
    # Add import for get_base_url from config
    if ($content -match "from mcp\.types import Tool") {
        $content = $content -replace "(from mcp\.types import Tool)", "`$1`nfrom ..config import get_base_url"
        $updated = $true
    }
    
    # Replace placeholder URLs in schemas with your actual URL
    $oldPlaceholders = @(
        "https://your-commerce-site\.com",
        "https://example\.com", 
        "https://your-dynamics365-site\.com"
    )
    
    foreach ($placeholder in $oldPlaceholders) {
        if ($content -match $placeholder) {
            $content = $content -replace $placeholder, "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
            $updated = $true
        }
    }
    
    # Update handle_tool methods to use get_base_url()
    $handleToolPatterns = @(
        'arguments\.get\("baseUrl",\s*"https://your-commerce-site\.com"\)',
        'arguments\.get\("baseUrl",\s*"https://example\.com"\)',
        'arguments\.get\("baseUrl",\s*"https://your-dynamics365-site\.com"\)',
        'arguments\.get\(''baseUrl'',\s*''https://your-commerce-site\.com''\)',
        'arguments\.get\(''baseUrl'',''https://your-commerce-site\.com''\)'
    )
    
    foreach ($pattern in $handleToolPatterns) {
        if ($content -match $pattern) {
            $content = $content -replace $pattern, 'arguments.get("baseUrl", get_base_url())'
            $updated = $true
        }
    }
    
    # Save the file if it was updated
    if ($updated) {
        $content | Set-Content $controller.FullName -NoNewline
        Write-Host "    ✓ Updated $($controller.Name)"
    } else {
        Write-Host "    - No changes needed for $($controller.Name)"
    }
}

Write-Host "`nCompleted! All controllers now use centralized base URL configuration."
Write-Host "Base URL is set to: https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
