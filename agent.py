import json
import time


# -----------------------------
# Mock database
# -----------------------------

VENDORS = {
    "ABC Supplies": {
        "status": "verified",
        "bank_account": "XXXX1234"
    },
    "XYZ Ltd": {
        "status": "verified",
        "bank_account": "XXXX5678"
    }
}

PREVIOUS_INVOICES = [
    {
        "invoice_number": "INV-1001",
        "vendor": "ABC Supplies",
        "amount": 25000
    }
]


# -----------------------------
# Tools
# -----------------------------

def check_vendor(invoice):
    print("🔍 Checking vendor...")
    time.sleep(1)

    vendor = VENDORS.get(invoice["vendor"])

    if not vendor:
        return {
            "status": "error",
            "result": "Vendor not found",
            "evidence": "Vendor does not exist in internal database"
        }

    return {
        "status": "success",
        "result": "Vendor verified",
        "evidence": f"Vendor {invoice['vendor']} exists in the verified vendor database"
    }


def check_duplicate(invoice):
    print("🔍 Checking for duplicate invoice...")
    time.sleep(1)

    for previous in PREVIOUS_INVOICES:
        if (
            previous["invoice_number"] == invoice["invoice_number"]
            and previous["vendor"] == invoice["vendor"]
        ):
            return {
                "status": "success",
                "result": "Duplicate detected",
                "evidence": "Matching invoice number and vendor found"
            }

    return {
        "status": "success",
        "result": "No duplicate found",
        "evidence": "No matching invoice found in previous records"
    }


def check_risk(invoice):
    print("🔍 Assessing risk...")
    time.sleep(1)

    if invoice["amount"] > 100000:
        return {
            "status": "success",
            "result": "High risk",
            "evidence": "Invoice amount exceeds ₹1,00,000"
        }

    return {
        "status": "success",
        "result": "Low risk",
        "evidence": "Invoice amount is within normal range"
    }


# -----------------------------
# Agent
# -----------------------------

def investigate_invoice(invoice):

    steps = []

    print("\n🤖 AP INVESTIGATION AGENT")
    print("-" * 40)

    # Agent decides to verify vendor first
    steps.append("Agent decided to verify vendor")

    vendor_result = check_vendor(invoice)
    steps.append(vendor_result)

    # If vendor is invalid → escalate
    if vendor_result["result"] != "Vendor verified":
        return {
            "decision": "ESCALATE",
            "reason": "Vendor verification failed",
            "steps": steps
        }

    # Agent decides to check duplicates
    steps.append("Agent decided to check for duplicates")

    duplicate_result = check_duplicate(invoice)
    steps.append(duplicate_result)

    if duplicate_result["result"] == "Duplicate detected":
        return {
            "decision": "REJECT",
            "reason": "Duplicate invoice detected",
            "steps": steps
        }

    # Agent decides to assess risk
    steps.append("Agent decided to perform risk assessment")

    risk_result = check_risk(invoice)
    steps.append(risk_result)

    if risk_result["result"] == "High risk":
        return {
            "decision": "ESCALATE",
            "reason": "High-value invoice requires human approval",
            "steps": steps
        }

    return {
        "decision": "APPROVE",
        "reason": "Invoice passed vendor, duplicate and risk checks",
        "steps": steps
    }


# -----------------------------
# Demo
# -----------------------------

if __name__ == "__main__":

    invoice = {
        "invoice_number": "INV-2001",
        "vendor": "ABC Supplies",
        "amount": 25000
    }

    result = investigate_invoice(invoice)

    print("\n" + "=" * 40)
    print("FINAL DECISION:", result["decision"])
    print("REASON:", result["reason"])
    print("=" * 40)