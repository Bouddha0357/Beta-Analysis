import streamlit as st
import yfinance as yf
import pandas as pd

# Example list — replace with full ASX tickers
ASX_TICKERS = ['ACF.AX', 	'ADH.AX', 	'AGL.AX', 	'AHX.AX', 	'AIA.AX', 	'AIZ.AX', 	'ANG.AX', 	'ANN.AX', 	'APA.AX', 	'ARB.AX', 	'ARF.AX', 	'BAP.AX', 	'BGA.AX', 	'BHP.AX', 	'BKW.AX', 	'BLX.AX', 	'BPT.AX', 	'BRG.AX', 	'BRI.AX', 	'BSL.AX', 	'BXB.AX', 	'CAA.AX', 	'CAJ.AX', 	'CAR.AX', 	'CBO.AX', 	'CDP.AX', 	'CEN.AX', 	'CHC.AX', 	'CKF.AX', 	'CLW.AX', 	'CLX.AX', 	'CNI.AX', 	'CNU.AX', 	'COL.AX', 	'CPU.AX', 	'CQE.AX', 	'CSL.AX', 	'CWY.AX', 	'CYG.AX', 	'D2O.AX', 	'DBF.AX', 	'DDR.AX', 	'DJRE.AX', 	'DMP.AX', 	'DUR.AX', 	'DXC.AX', 	'DXI.AX', 	'EBG.AX', 	'EBO.AX', 	'ECH.AX', 	'EGH.AX', 	'EGN.AX', 	'ELD.AX', 	'FFI.AX', 	'FMG.AX', 	'FPH.AX', 	'FRI.AX', 	'FSF.AX', 	'FWD.AX', 	'GEM.AX', 	'GNE.AX', 	'GOR.AX', 	'GOZ.AX', 	'HCW.AX', 	'HDN.AX', 	'HNG.AX', 	'HPI.AX', 	'HSN.AX', 	'IDX.AX', 	'IGN.AX', 	'ILU.AX', 	'INA.AX', 	'IPH.AX', 	'IRE.AX', 	'JIN.AX', 	'JYC.AX', 	'KGN.AX', 	'KLS.AX', 	'KME.AX', 	'KSC.AX', 	'LAU.AX', 	'LBL.AX', 	'LLC.AX', 	'MAH.AX', 'MCY.AX', 	'MEZ.AX', 	'MFD.AX', 	'MGH.AX', 'MND.AX', 'MTS.AX', 	'MVA.AX', 	'MXI.AX', 	'MYE.AX', 	'MYG.AX', 	'NSR.AX', 	'NST.AX', 	'ORG.AX', 	'ORI.AX', 	'PMV.AX', 	'PPC.AX', 	'RFF.AX', 	'RGN.AX', 	'RHC.AX', 	'RIO.AX', 	'RMS.AX', 	'SCG.AX', 	'SGF.AX', 	'SGLLV.AX', 'SGM.AX', 'SHL.AX', 	'SIG.AX', 	'SNL.AX', 	'SNZ.AX', 	'SPK.AX', 	'SRH.AX', 	'STO.AX', 	'SUL.AX', 	'SXE.AX', 	'TAH.AX', 	'TBR.AX', 	'TCL.AX', 	'THL.AX', 	'TLC.AX', 	'TLS.AX', 	'TPG.AX', 	'TRA.AX', 	'TWD.AX', 	'TWE.AX', 	'UOS.AX', 	'URF.AX', 	'VCX.AX', 	'WDS.AX', 	'WES.AX', 	'WOT.AX', 	'WOW.AX', 'WTC.AX', 'XRF.AX', ]

st.title("ASX 5‑Year Beta Downloader 📊")

@st.cache_data
def fetch_betas(tickers):
    data = {}
    for t in tickers:
        info = yf.Ticker(t).info
        beta = info.get('beta', None)
        data[t] = beta
    df = pd.DataFrame.from_dict(data, orient='index', columns=['5Y Beta'])
    df.index.name = 'Ticker'
    return df

beta_df = fetch_betas(ASX_TICKERS)
st.write("Here are the beta values Yahoo Finance provides:")
st.table(beta_df)

# Prepare CSV for download
@st.cache_data
def to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv().encode('utf-8')

csv_bytes = to_csv_bytes(beta_df)

st.download_button(
    label="📥 Download beta values as CSV",
    data=csv_bytes,
    file_name="asx_5y_betas.csv",
    mime="text/csv"
)
