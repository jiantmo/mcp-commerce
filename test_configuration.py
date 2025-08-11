#!/usr/bin/env python3
"""
Test configuration system for Dynamics 365 Commerce MCP Server
"""

import os
import sys
from mcp_dynamics365_commerce_server.config import get_config, CommerceConfig

def test_no_configuration():
    """Test when no environment variable is set"""
    print("Testing with no configuration...")
    
    # Clear any existing env vars
    for var in ['DYNAMICS365_BASE_URL', 'COMMERCE_BASE_URL', 'D365_BASE_URL']:
        if var in os.environ:
            del os.environ[var]
    
    # Create fresh config
    config = CommerceConfig()
    
    print(f"Base URL: {config.base_url}")
    print(f"Is configured: {config.is_configured}")
    
    is_valid, message = config.validate_config()
    print(f"Validation: {is_valid} - {message}")
    print()

def test_with_configuration():
    """Test with environment variable set"""
    print("Testing with DYNAMICS365_BASE_URL configured...")
    
    # Set environment variable
    os.environ['DYNAMICS365_BASE_URL'] = 'https://contoso.commerce.dynamics.com'
    
    # Create fresh config
    config = CommerceConfig()
    
    print(f"Base URL: {config.base_url}")
    print(f"Is configured: {config.is_configured}")
    
    is_valid, message = config.validate_config()
    print(f"Validation: {is_valid} - {message}")
    
    # Test API endpoint generation
    endpoint = config.get_api_endpoint('Customers/Search')
    print(f"Sample API endpoint: {endpoint}")
    print()

def test_placeholder_url():
    """Test with placeholder URL"""
    print("Testing with placeholder URL...")
    
    os.environ['DYNAMICS365_BASE_URL'] = 'https://your-commerce-site.com'
    
    config = CommerceConfig()
    
    print(f"Base URL: {config.base_url}")
    print(f"Is configured: {config.is_configured}")
    
    is_valid, message = config.validate_config()
    print(f"Validation: {is_valid} - {message}")
    print()

def test_invalid_url():
    """Test with invalid URL"""
    print("Testing with invalid URL...")
    
    os.environ['DYNAMICS365_BASE_URL'] = 'http://insecure-site.com'
    
    config = CommerceConfig()
    
    print(f"Base URL: {config.base_url}")
    print(f"Is configured: {config.is_configured}")
    
    is_valid, message = config.validate_config()
    print(f"Validation: {is_valid} - {message}")
    print()

def test_alternative_env_vars():
    """Test alternative environment variable names"""
    print("Testing alternative environment variables...")
    
    # Clear primary var
    if 'DYNAMICS365_BASE_URL' in os.environ:
        del os.environ['DYNAMICS365_BASE_URL']
    
    # Test COMMERCE_BASE_URL
    os.environ['COMMERCE_BASE_URL'] = 'https://fabrikam.commerce.dynamics.com'
    config = CommerceConfig()
    print(f"COMMERCE_BASE_URL: {config.base_url}")
    
    # Clear and test D365_BASE_URL
    del os.environ['COMMERCE_BASE_URL']
    os.environ['D365_BASE_URL'] = 'https://adventureworks.commerce.dynamics.com'
    config = CommerceConfig()
    print(f"D365_BASE_URL: {config.base_url}")
    print()

def main():
    """Run all configuration tests"""
    print("Configuration System Tests")
    print("=" * 50)
    
    test_no_configuration()
    test_with_configuration() 
    test_placeholder_url()
    test_invalid_url()
    test_alternative_env_vars()
    
    print("Configuration Help:")
    print("-" * 30)
    config = CommerceConfig()
    print(config.get_configuration_help())

if __name__ == "__main__":
    main()