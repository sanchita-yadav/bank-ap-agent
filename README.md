# 🏦 Bank AP Intelligence

An agentic Accounts Payable automation prototype that investigates invoices and makes intelligent approval decisions.

## Problem

Organizations process large volumes of invoices that require manual verification for vendor validity, duplicate invoices, and financial risk.

This process is time-consuming and prone to human error.

## Solution

Bank AP Intelligence uses an investigation agent to:

- Verify vendors
- Detect duplicate invoices
- Assess invoice risk
- Adapt when a verification service fails
- Decide whether an invoice should be approved, rejected, or escalated

## 🚀 Live Demo

[Open Bank AP Intelligence](https://bank-ap-agent-px79fmdycqjmnnetdqeuxr.streamlit.app)

## Agentic Workflow

User Invoice
→ Invoice Analysis
→ Agent Investigation
→ Tool Selection
→ Evidence Collection
→ Decision
→ Approval / Rejection / Escalation

If a tool fails, the agent can select a fallback verification method and continue the investigation.

## Demo Scenarios

| Scenario | Result |
|---|---|
| Normal Invoice | ✅ Approved |
| Duplicate Invoice | ❌ Rejected |
| High-Risk Invoice | ⚠️ Escalated |
| Vendor API Failure | 🔄 Fallback → Continue |

## Technology

- Python
- Streamlit
- Agent-based decision workflow
- Mock vendor and invoice databases

## Installation

Clone the repository:

```bash
git clone https://github.com/sanchita-yadav/bank-ap-agent.git
cd bank-ap-agent
