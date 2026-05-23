import streamlit as st
from datetime import datetime, timedelta

st.title("⏰ Manikanaku")

st.subheader("Working Time Calculator")

# -----------------------------
# Working Time Inputs
# -----------------------------

start_time = st.text_input("Starting Time (HH:MM:SS)", "07:15:00")
start_ampm = st.selectbox("Start Time AM/PM", ["AM", "PM"])

end_time = st.text_input("Ending Time (HH:MM:SS)", "05:30:00")
end_ampm = st.selectbox("End Time AM/PM", ["AM", "PM"])

# -----------------------------
# Break Time Inputs
# -----------------------------

st.subheader("Break Time")

break_start = st.text_input("Break Start Time", "12:00:00")
break_start_ampm = st.selectbox("Break Start AM/PM", ["AM", "PM"])

break_end = st.text_input("Break End Time", "12:45:00")
break_end_ampm = st.selectbox("Break End AM/PM", ["AM", "PM"])

# -----------------------------
# Price Input
# -----------------------------

price_per_hour = st.number_input("Price Per Hour ₹", min_value=0.0, value=150.0)

# -----------------------------
# Calculate Button
# -----------------------------

if st.button("Calculate"):

    try:

        # Convert Start Time
        start = datetime.strptime(
            start_time + " " + start_ampm,
            "%I:%M:%S %p"
        )

        # Convert End Time
        end = datetime.strptime(
            end_time + " " + end_ampm,
            "%I:%M:%S %p"
        )

        # Convert Break Times
        break_s = datetime.strptime(
            break_start + " " + break_start_ampm,
            "%I:%M:%S %p"
        )

        break_e = datetime.strptime(
            break_end + " " + break_end_ampm,
            "%I:%M:%S %p"
        )

        # If end time next day
        if end < start:
            end += timedelta(days=1)

        # If break end next day
        if break_e < break_s:
            break_e += timedelta(days=1)

        # Total Working Time
        total_time = end - start

        # Break Duration
        break_time = break_e - break_s

        # Final Working Time
        final_work = total_time - break_time

        # Convert to Hours
        total_seconds = final_work.total_seconds()

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        # Salary Calculation
        total_hours = total_seconds / 3600
        total_salary = total_hours * price_per_hour

        # -----------------------------
        # Results
        # -----------------------------

        st.success("Calculation Completed")

        st.write(f"🕒 Total Time: {total_time}")
        st.write(f"☕ Break Time: {break_time}")

        st.write(
            f"✅ Working Time: {hours} Hours "
            f"{minutes} Minutes "
            f"{seconds} Seconds"
        )

        st.write(f"💰 Total Salary: ₹ {total_salary:.2f}")

    except:
        st.error("Please enter correct time format HH:MM:SS")