import streamlit as st

st.set_page_config(page_title="PMMVY Digital Assistant", layout="wide")

st.title("PMMVY Digital Assistant")
st.subheader("Role-Based Counselling & Scheme Support Tool")

# Initialize session state
if "role" not in st.session_state:
    st.session_state.role = None

# Role Selection
if st.session_state.role is None:
    st.write("Please select your role:")
    if st.button("Anganwadi Worker (AWW)"):
        st.session_state.role = "AWW"
    if st.button("Lady Supervisor (LS)"):
        st.session_state.role = "LS"

# AWW Interface
if st.session_state.role == "AWW":
    st.success("Logged in as: Anganwadi Worker")

    option = st.selectbox("Choose Topic", [
        "PMMVY Enrollment Process",
        "Installment & Rejection FAQs",
        "Required Documents",
        "Nutrition Counselling Support",
        "High-Risk Pregnancy Red Flags",
        "Escalation & Grievance Process"
    ])

    if option == "PMMVY Enrollment Process":
        st.write("""
        Steps:
        1. Verify LMP and eligibility.
        2. Collect Aadhaar, Bank Details.
        3. Register beneficiary in portal.
        4. Ensure MCP card updated.
        """)

    elif option == "Installment & Rejection FAQs":
        st.write("""
        Common Rejection Reasons:
        - Aadhaar mismatch
        - Bank account error
        - Duplicate entry
        - Incorrect LMP
        """)

    elif option == "Required Documents":
        st.write("""
        Required Documents:
        - Aadhaar Card
        - MCP Card
        - Bank Passbook
        - Pregnancy confirmation
        """)

    elif option == "Nutrition Counselling Support":
        st.write("""
        Balanced Diet:
        - Grains, pulses, vegetables, fruits, milk daily
        - IFA from 2nd trimester
        - Calcium twice daily
        - Minimum 4 ANC visits
        """)

    elif option == "High-Risk Pregnancy Red Flags":
        st.write("""
        Immediate Referral If:
        - Swelling of face
        - Severe headache
        - Bleeding
        - Reduced fetal movement
        """)

    elif option == "Escalation & Grievance Process":
        st.write("""
        If grievance >30 days:
        - Inform LS
        - Update portal
        - Escalate to CDPO
        """)

# LS Interface
elif st.session_state.role == "LS":
    st.success("Logged in as: Lady Supervisor")

    option = st.selectbox("Choose Topic", [
        "Approval Workflow",
        "Common AWW Errors",
        "Pendency Monitoring",
        "Grievance Handling",
        "Counselling Supervision Checklist"
    ])

    if option == "Approval Workflow":
        st.write("""
        Review:
        - Documents verified
        - Eligibility confirmed
        - No duplicate entry
        Approve within timeline.
        """)

    elif option == "Common AWW Errors":
        st.write("""
        Frequent Errors:
        - Incomplete documents
        - Wrong bank details
        - Late entry
        """)

    elif option == "Pendency Monitoring":
        st.write("""
        Monitor:
        - AWW level pending cases
        - Approval delay >7 days
        - Sector performance ranking
        """)

    elif option == "Grievance Handling":
        st.write("""
        Track grievances weekly.
        Escalate cases pending >30 days.
        """)

    elif option == "Counselling Supervision Checklist":
        st.write("""
        Ensure AWW:
        ✔ Conducted nutrition counselling
        ✔ Distributed IFA
        ✔ Updated MCP card
        ✔ Recorded ANC visits
        """)

# Reset Button
if st.button("Change Role"):
    st.session_state.role = None
