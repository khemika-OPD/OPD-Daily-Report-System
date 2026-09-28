import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="OPD Daily Report", layout="wide")

st.title("🏥 ระบบบันทึกรายงานประจำวัน OPD")
st.subheader(f"วันที่: {date.today().strftime('%d/%m/%Y')}")

# --- ส่วนที่ 1: ข้อมูลทั่วไป ---
st.header("1. สถิติการคัดกรอง")
col1, col2 = st.columns(2)
with col1:
    scr_gen = st.number_input("ซักประวัติทั่วไป", min_value=0, step=1)
    scr_wheel = st.number_input("ซักประวัติจุดรถนั่ง-รถนอน", min_value=0, step=1)
with col2:
    scr_spec = st.number_input("ซักประวัติคลินิกพิเศษ", min_value=0, step=1)
    scr_99 = st.number_input("ซักประวัติจุด 99", min_value=0, step=1)
total_scr = scr_gen + scr_wheel + scr_spec + scr_99
st.info(f"รวมยอดซักประวัติ: {total_scr} ราย")

# --- ส่วนที่ 2: การจัดการเร่งด่วน ---
st.header("2. การจัดการเร่งด่วน")
c1, c2 = st.columns(2)
fast_track = c1.number_input("Fast track OPD", min_value=0)
send_er = c2.number_input("ส่ง ER", min_value=0)

# --- ส่วนที่ 3: นัดหมายและผ่าตัด ---
st.header("3. นัดหมายและเตรียมตัวผ่าตัด")
col_a, col_b, col_c = st.columns(3)
pre_op = col_a.number_input("Pre-op เคส OR", min_value=0)
set_or = col_b.number_input("นัดผ่าตัด", min_value=0)
egd = col_c.number_input("นัดส่องกล้อง", min_value=0)
us = col_a.number_input("นัด U/S", min_value=0)
mri = col_b.number_input("นัด MRI", min_value=0)
echo = col_c.number_input("นัด echo", min_value=0)
ct = col_a.number_input("นัด CT", min_value=0)

# --- ส่วนที่ 4: Admit ---
st.header("4. Admit")
admit_case = st.number_input("จำนวนผู้ป่วย Admit", min_value=0)

# --- ส่วนที่ 5: แยกตามสาขา ---
st.header("5. สถิติผู้ป่วยพบแพทย์แยกตามสาขา")
branches = ["OPD ทั่วไป", "Ortho", "Ped", "Med", "นรีเวช", "ศัลยกรรม", "เวชฟื้นฟู"]
branch_data = {}
cols = st.columns(len(branches))
for i, branch in enumerate(branches):
    branch_data[branch] = cols[i].number_input(branch, min_value=0)

# --- ส่วนที่ 6: งานหัตถการ ---
st.header("6. งานหัตถการประจำวัน")
h_cols = st.columns(4)
proc_names = ["ทำแผล", "ล้างตา", "ฉีดยา", "EKG", "ถอดเล็บ", "I&D", "Excision", "Suture", "Remove FB"]
proc_data = {}
for i, p in enumerate(proc_names):
    proc_data[p] = h_cols[i % 4].number_input(p, min_value=0)

# --- ส่วนที่ 7 & 8: งานเปล & อื่นๆ ---
st.header("7. บริการงานเปล และ 8. บริการอื่นๆ")
col_v1, col_v2 = st.columns(2)
with col_v1:
    st.write("**งานเปล**")
    wheel = st.number_input("รถนั่ง", min_value=0)
    stretcher = st.number_input("รถนอน", min_value=0)
with col_v2:
    st.write("**บริการพิเศษ**")
    telemed = st.number_input("Telemed", min_value=0)
    rrt = st.number_input("RRT", min_value=0)

# --- ปุ่มสรุปรายงาน ---
if st.button("สรุปรายงานสำหรับคัดลอกลง LINE"):
    report_text = f"""
📌 **รายงาน OPD ประจำวันที่ {date.today()}**
1. สถิติการคัดกรอง: รวม {total_scr} ราย
2. เร่งด่วน: Fast track {fast_track}, ส่ง ER {send_er}
3. นัดหมาย: Pre-op {pre_op}, CT {ct}, MRI {mri}
4. Admit: {admit_case} ราย
5. แยกสาขา: Med({branch_data['Med']}), Ortho({branch_data['Ortho']}), Ped({branch_data['Ped']})
6. หัตถการ: ทำแผล({proc_data['ทำแผล']}), ฉีดยา({proc_data['ฉีดยา']})
    """
    st.code(report_text) # แสดงผลเป็นช่องให้ก๊อปปี้ง่ายๆ
