"""
Device Configuration Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (2 total):
1. device_configuration_get_device_configuration - Gets a single device configuration
2. device_configuration_update_device_configuration - Update device configuration settings

This controller handles device configuration operations for POS and terminal settings.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool

class DeviceConfigurationController:
    """Controller for Device Configuration-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of device configuration-related tools"""
        return [
            Tool(
                name="device_configuration_get_device_configuration",
                description="Gets a single device configuration",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "deviceId": {
                            "type": "string",
                            "description": "Device identifier (optional)"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="device_configuration_update_device_configuration",
                description="Update device configuration settings",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "deviceId": {"type": "string"},
                        "configuration": {"type": "object"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["deviceId", "configuration"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle device configuration tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "device_configuration_get_device_configuration":
            device_id = arguments.get("deviceId", f"DEVICE_{random.randint(1000, 9999)}")
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/DeviceConfiguration",
                "deviceId": device_id,
                "deviceConfiguration": {
                    "deviceId": device_id,
                    "deviceName": f"POS Terminal {device_id[-4:]}",
                    "deviceType": "POS",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "registerId": f"REG{random.randint(100, 999)}",
                    "terminalId": f"TERM{random.randint(100, 999)}",
                    "isActive": True,
                    "lastConnected": datetime.now().isoformat() + "Z",
                    "firmwareVersion": f"2.{random.randint(1, 9)}.{random.randint(0, 99)}",
                    "applicationVersion": f"10.{random.randint(0, 9)}.{random.randint(1000, 9999)}.{random.randint(1, 999)}",
                    "operatingSystem": "Windows 10 IoT Enterprise",
                    "hardwareProfile": {
                        "profileId": "HWPROF001",
                        "profileName": "Standard POS Profile",
                        "receiptPrinter": {
                            "enabled": True,
                            "printerName": "Epson TM-T88VI",
                            "connectionType": "USB",
                            "paperWidth": "80mm",
                            "autocut": True
                        },
                        "cashDrawer": {
                            "enabled": True,
                            "drawerName": "Star SMD2-1317",
                            "connectionType": "RJ12",
                            "openCommand": "Pulse"
                        },
                        "barcodeScanner": {
                            "enabled": True,
                            "scannerName": "Honeywell Voyager 1202g",
                            "connectionType": "USB",
                            "autoTrigger": True
                        },
                        "cardPaymentDevice": {
                            "enabled": True,
                            "deviceName": "Ingenico iSC250",
                            "connectionType": "USB",
                            "supportedCards": ["Visa", "MasterCard", "American Express", "Discover"],
                            "supportsPinPad": True,
                            "supportsContactless": True
                        },
                        "customerDisplay": {
                            "enabled": True,
                            "displayName": "Logic Controls PD3900",
                            "connectionType": "USB",
                            "displayLines": 2,
                            "charactersPerLine": 20
                        },
                        "scale": {
                            "enabled": False,
                            "scaleName": None,
                            "connectionType": None
                        }
                    },
                    "functionalProfile": {
                        "profileId": "FUNCPROF001",
                        "profileName": "Standard Functional Profile",
                        "allowSalesWithoutCustomer": True,
                        "allowVoidTransactions": True,
                        "allowDiscounts": True,
                        "maxDiscountPercent": 20.0,
                        "requireManagerApproval": True,
                        "allowReturns": True,
                        "returnTimeLimitDays": 30,
                        "allowLayaway": True,
                        "allowQuotes": True,
                        "allowSuspendTransactions": True,
                        "allowRecallTransactions": True,
                        "enableInventoryLookup": True,
                        "enablePriceCheck": True,
                        "maxCashAmount": 10000.00,
                        "allowOverTenderAmount": 100.00,
                        "requireSignatureAmount": 25.00
                    },
                    "visualProfile": {
                        "profileId": "VISPROF001",
                        "profileName": "Standard Visual Profile",
                        "theme": "Modern Blue",
                        "buttonLayout": "Grid",
                        "showCustomerPanel": True,
                        "showProductSearch": True,
                        "showTransactionList": True,
                        "fontSize": "Medium",
                        "highContrast": False,
                        "touchEnabled": True,
                        "keyboardShortcuts": True
                    },
                    "networkConfiguration": {
                        "connectionType": "Ethernet",
                        "ipAddress": f"192.168.1.{random.randint(100, 254)}",
                        "subnetMask": "255.255.255.0",
                        "gateway": "192.168.1.1",
                        "dnsServers": ["8.8.8.8", "8.8.4.4"],
                        "proxyEnabled": False,
                        "httpsRequired": True,
                        "serverUrl": base_url,
                        "cloudSyncEnabled": True,
                        "offlineCapable": True
                    },
                    "securitySettings": {
                        "encryptionEnabled": True,
                        "encryptionLevel": "AES-256",
                        "certificateInstalled": True,
                        "certificateExpiry": (datetime.now().replace(year=datetime.now().year + 1)).isoformat() + "Z",
                        "userAuthenticationRequired": True,
                        "sessionTimeoutMinutes": 30,
                        "passwordComplexityRequired": True,
                        "auditingEnabled": True,
                        "deviceLockEnabled": True,
                        "remoteWipeCapable": True
                    },
                    "peripheralStatus": {
                        "receiptPrinter": {"status": "Online", "lastChecked": datetime.now().isoformat() + "Z"},
                        "cashDrawer": {"status": "Closed", "lastChecked": datetime.now().isoformat() + "Z"},
                        "barcodeScanner": {"status": "Ready", "lastChecked": datetime.now().isoformat() + "Z"},
                        "cardPaymentDevice": {"status": "Online", "lastChecked": datetime.now().isoformat() + "Z"},
                        "customerDisplay": {"status": "Active", "lastChecked": datetime.now().isoformat() + "Z"}
                    },
                    "maintenanceInfo": {
                        "lastMaintenance": (datetime.now().replace(day=1)).isoformat() + "Z",
                        "nextScheduledMaintenance": (datetime.now().replace(month=datetime.now().month + 1, day=1)).isoformat() + "Z",
                        "warrantyExpiration": (datetime.now().replace(year=datetime.now().year + 2)).isoformat() + "Z",
                        "supportContact": "+1-800-555-SUPPORT",
                        "vendorInfo": {
                            "manufacturer": "Contoso POS Systems",
                            "model": "CPS-5000",
                            "serialNumber": f"CPS{random.randint(100000, 999999)}",
                            "purchaseDate": "2023-06-15T00:00:00Z"
                        }
                    },
                    "configurationStatus": {
                        "isConfigured": True,
                        "lastConfigurationUpdate": datetime.now().isoformat() + "Z",
                        "configurationVersion": "1.2.3",
                        "pendingUpdates": False,
                        "healthStatus": "Healthy",
                        "lastHealthCheck": datetime.now().isoformat() + "Z",
                        "alerts": [],
                        "recommendations": [
                            "Consider updating firmware to latest version",
                            "Schedule monthly maintenance check"
                        ]
                    }
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "DeviceConfiguration",
                    "description": "Gets a single device configuration"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "device_configuration_update_device_configuration":
            device_id = arguments.get("deviceId")
            config = arguments.get("configuration", {})
            
            return {
                "api": f"PUT {base_url}/api/CommerceRuntime/DeviceConfiguration/{device_id}",
                "deviceId": device_id,
                "updated": True,
                "configuration": config,
                "timestamp": datetime.now().isoformat() + "Z"
            }
        else:
            return {"error": f"Unknown device configuration tool: {name}"}