import streamlit as st
from agent import investigate_invoice

st.set_page_config(
    page_title="Bank AP Intelligence",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank AP Intelligence")
st.caption("AI-powered Accounts Payable Investigation Agent")

st.divider()

# -----------------------------
# Demo Scenario
# -----------------------------

st.subheader("📋 Invoice Investigation")

scenario = st.selectbox(
    "Choose Demo Scenario",
    [
        "Normal Invoice",
        "Duplicate Invoice",
        "High-Risk Invoice",
        "Vendor API Failure"
    ]
)

if scenario == "Normal Invoice":
    invoice_number = "INV-2002"
    vendor = "ABC Supplies"
    amount = 25000
    simulate_failure = False

elif scenario == "Duplicate Invoice":
    invoice_number = "INV-1001"
    vendor = "ABC Supplies"
    amount = 25000
    simulate_failure = False

elif scenario == "High-Risk Invoice":
    invoice_number = "INV-3001"
    vendor = "XYZ Ltd"
    amount = 250000
    simulate_failure = False

else:
    invoice_number = "INV-4001"
    vendor = "ABC Supplies"
    amount = 25000
    simulate_failure = True


# -----------------------------
# Show Invoice
# -----------------------------

st.write(f"**Invoice Number:** {invoice_number}")
st.write(f"**Vendor:** {vendor}")
st.write(f"**Amount:** ₹{amount:,}")

st.divider()


# -----------------------------
# Investigation
# -----------------------------

if st.button("🤖 Investigate Invoice", use_container_width=True):

    invoice = {
        "invoice_number": invoice_number,
        "vendor": vendor,
        "amount": amount,
        "simulate_failure": simulate_failure
    }

    with st.spinner("Agent investigating invoice..."):
        result = investigate_invoice(invoice)

    st.divider()

    st.subheader("🤖 Agent Activity")

    for step in result["steps"]:

        if isinstance(step, str):
            st.info("→ " + step)

        else:
            if step["status"] == "success":
                st.success(
                    f'✓ {step["result"]}\n\n'
                    f'{step["evidence"]}'
                )

            else:
                st.error(
                    f'⚠ {step["result"]}\n\n'
                    f'{step["evidence"]}'
                )

    st.divider()

    # -----------------------------
    # Final Decision
    # -----------------------------

    st.subheader("Final Decision")

    decision = result["decision"]

    if decision == "APPROVE":

        st.success(
            f"✅ APPROVED\n\n{result['reason']}"
        )

    elif decision == "REJECT":

        st.error(
            f"❌ REJECTED\n\n{result['reason']}"
        )

    else:

        st.warning(
            f"⚠️ ESCALATED\n\n{result['reason']}"
        )