def fallback_vendor_check(invoice):
    print("🔄 Using fallback vendor database...")

    vendor = VENDORS.get(invoice["vendor"])

    if vendor:
        return {
            "status": "success",
            "result": "Vendor verified using fallback",
            "evidence": "Internal vendor database confirmed the vendor"
        }

    return {
        "status": "error",
        "result": "Vendor could not be verified",
        "evidence": "Vendor not found in fallback database"
    }