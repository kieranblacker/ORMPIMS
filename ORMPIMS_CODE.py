# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters v2.0
#name,bname,type,family,measurement,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#DeclarationsEnd
#
# SOLVER CODE:
# ============
#
# 1. Import Libraries
#=====================
from TechlogMath import *
from Techlog import MissingValue
import math
from math import exp
#import numpy
#import scipy
#
# 2. FORMATION & WELLBORE PROPERTIES:
#====================================
#
# 2.1 Set True Vertical Depth:
#=============================
def fTrueVerticalDepth(MD,TVD):
	"""
	Inputs:
	1. MD : Measured Depth
	2. TVD : True Vertical Depth
	Outputs:
	1. TVD: True Vertical Depth
	"""
	if (TVD ==MissingValue):
		return MD
	else:
		return TVD
#
# 2.2 Formation Temperature:
#============================
def fFormationTemperature(Method,TVD,SD,ST,TG): 
	"""
	Inputs:
	1. Method
	2. TVD : True Vertical Depth
	3. SD: Start Depth
	4. ST: Start Temperature
	5. TG: Temperature Gradient
	Outputs:
	1. FT: Formation Temperature
	"""
	if(Method=="1. Fix at Start Temperature"):
		FT=ST
	else:
		FT=ST+(TVD-SD)*TG
	return FT
#
# 2.3 Formation Pressure
#==========================
def fFormationPressure(Method,TVD,SD,SP,PG): 
	"""
	Inputs:
	1. Method
	2. TVD : True Vertical Depth
	3. SD: Start Depth
	4. SP: Start Pressure
	5. PG: Pressure Gradient
	Outputs:
	1. FP: Formation Pressure
	"""
	if(Method=="1. Fix at Start Pressure"):
		FP=SP
	else:
		FP=SP+(TVD-SD)*PG
	return FP
#
# 3. FLUID PROPERTIES:
#=====================
#
# 3.1 Compute Water Properties:
#==============================
def fWaterProperties(Set_Rw,Set_Rw_Temperature,GasWaterRatio,Temperature,Pressure): 
	"""
	Inputs:
	1. Set_Rw: Water Resistivity at temperature RwT (ohm.m)
	2. Set_Rw_Temperature: Temperature (degC)
	3. GasWaterRatio: Gas Water Ratio (v/v)
	4. Temperature: Temperature (Deg C)
	5. Pressure: Pressure (Psi)
	Outputs:
	1. Rw: Temperature Corrected Rw (Ohm.m)
	2. Salinity: Salinity (kppm)
	3. Dw: Density of Water (g/cc)
	4. HIw: Hydrogen Index of Water (Frac)
	5. DTw: Compressional Slowness of Water (us/ft)
	"""
	Rw=fRwTemperatureCorrected(Set_Rw,Set_Rw_Temperature,Temperature)
	Salinity=fComputeSalinity(Set_Rw,Set_Rw_Temperature)
	Dw=fWaterDensity(Salinity, GasWaterRatio, Temperature, Pressure)
	HIw=fWaterHydrogenIndex(Salinity, GasWaterRatio, Temperature, Pressure)
	Vpw=fWaterAcousticVelocity(Salinity, GasWaterRatio, Temperature, Pressure) # Vp of water in m.s-1
	Dtw=1000000/(3.281*Vpw) # Compressional slowness of water in us/ft
#	
	return Rw,Salinity,Dw,HIw,Dtw
#
# 3.2 Compute Hydrocarbon Properties:
#====================================
def fHydrocarbonProperties(GasGravity,API,GasOilRatio,Temperature,Pressure): 
	"""
	Inputs: 
	1. GasGravity: Gas Gravity
	2. API: Oil API
	3. GasOilRatio: Gas Oil Ratio (v/v)
	4. Temperature: Temperature (Deg C)
	5. Pressure: Pressure (Psi)
	Outputs:
	1. Dg: Gas Density (g/cc)
	2. HIg: Gas Hydrogen Index (frac)
	3. GOR: Gas Oil Ratio (scf/bbl)
	4. Dtg: Gas Compressional Slowness (us/ft)
	4. Do: Oil Density (g/cc)
	5. HIo: Oil Hydrogen Index (frac)
	6. Dto: Oil Compressional Slowness (us/ft)
	"""
	Dg=fGasDensity(GasGravity, Temperature, Pressure)
	HIg=fGasHydrogenIndex(GasGravity, Temperature, Pressure)
	MaxGOR=fMaxGasOilRatio(API, GasGravity, Temperature, Pressure)
	GOR=ImposeLimits(GasOilRatio,0,MaxGOR)
	Vpg=fGasAcousticVelocity(GasGravity, Temperature, Pressure) # P-Wave Acoustic Velocity of gas in m/s
	Dtg=1000000/(3.281*Vpg) # Compressional slowness of gas in us/ft
	Do=fOilDensity(API, GOR, GasGravity, Temperature, Pressure)
	HIo=fOilHydrogenIndex(Do)
	Vpo=fOilAcousticVelocity(API, GOR, GasGravity, Temperature, Pressure) # P-Wave Acoustic Velocity of oil in m/s
	Dto=1000000/(3.281*Vpo) # Compressional slowness of oil in us/ft
	return Dg,HIg,Dtg,Do,HIo,Dto,GOR
#
# 3.3 Evaluate Borehole Quality:
#===============================
def BoreHoleQuality(Cali,Dcor,Method,BitSize,MaxWashout,MaxDcor): 
	"""
	Inputs: 
	1. Cali:		Caliper (in)
	2. Dcor:		Density Correction (g/cm3)
	3. Method:		Badhole Method
	4. BitSize:		Nominal borehole diameter (in)
	5. MaxWashout:  Maximum Difference between Cali ad Bitsize that is allowed before badhole is indicated
	6. MaxDcor:		Maximum allowed value of Dcor before badhole is indicated.
	Outputs:
	1. FCalc:		Flag indicating if computations will be allowed to proceed (=1) or not (=0)
	2. BHF:			Bad hole flag. BHF=0 if the hole is ok, and BHF=1 if it is not ok.
	"""
#	1. Initialise:
	FCalc=1
	BHF=0
#	2. Calculate BHF Information:
	if MissingValue in (Cali,BitSize,MaxWashout):
		BHF_Caliper=0
	else:
		BHF_Caliper_Washout=Cali-BitSize
		if(BHF_Caliper_Washout>MaxWashout):
			BHF_Caliper=1
		else:
			BHF_Caliper=0
#
	if MissingValue in (Dcor,MaxDcor):
		BHF_Dcor=0
	else:
		if(Dcor>MaxDcor):
			BHF_Dcor=1
		else:
			BHF_Dcor=0
#
#	3. Asssign final BHF:
	if (Method=="1. Off"):
		BHF=0
	if (Method=="2. On - Caliper Only"):
		BHF=BHF_Caliper
	if (Method=="3. On - Density Correction Only"):
		BHF=BHF_Dcor
	if (Method=="4. On - Caliper and Density Correction"):
		if((BHF_Caliper==1) or (BHF_Dcor==1)):
			BHF=1
		else:
			BHF=0
	if (Method=="5. On - Badhole Assumed"):
		BHF=1
#
	return BHF
#
#
# 4. WIRELINE TOOL CORRECTIONS & ADDITIONAL PROPERTIES:
#======================================================
#
# 4.1 Neutron Porosity Excavation Corrections:
#=============================================
def ExcCorrected(ExC, Dm1, PHIe, HIpf):
	"""
	Inputs:
	1. ExC : Correction Flag ('Yes', 'No')
	2. Dm1 : Density Mineral1 (g/cc
	3. PHIe : Effective Porosity (v/v)
	4. HIpf : HI Pore Fluid (v/v)
	Outputs:
	1. Cf : PHIN Correction
	"""
	if ExC == "Yes":
		return ((Dm1/2.65)**2)*((2*(PHIe**2)*HIpf)+(0.04*PHIe))*(1-HIpf)
	else:
		return 0
#
# 4.2 Apparent Mud Filtrate & Formation Water Salinity Values:
#=============================================================
def Compute_RMFA_RWA(PHIt,Rxo,Rt,A,M):
	"""
	Inputs:
	1.  PHIt: Total porosity (frac)
	2.  Rxo: Shallow/Near Wellbore Resistivity
	3.	Rt:	Deep/Fprmation Water Resistivity
	4.	A: Lithology Constant.
	5.	M: Porosity Exponent.
	Outputs:
	1. 	Rmfa: Apparent mud filtrate resistivity.
	2. 	Rw: Apparent formation water resistivity.
	"""
	Rmfa=MissingValue
	Rwa=MissingValue
	if(Rxo==MissingValue):
		Rxo=Rt
	if MissingValue in (PHIt,Rxo,Rt,A,M):
		return Rmfa,Rwa
	Rmfa=((PHIt**M)/A)*Rxo
	Rwa=((PHIt**M)/A)*Rxo
	return Rmfa,Rwa
#
# 4.3 Compute Average Value:
#=============================================================		
def fGrainDensity(PAF,PAV):
	"""
	Inputs:
	1.  PAF: Matrix containing volume fractions
	2.  PAV: Matrix containing matrix values (e.g. Density)
	Outputs:
	1. 	AVAL: Average Value
	"""
	na=len(PAF)
	nb=len(PAV)
	AVAL=0
	SUM=0
	N=0
	if(na==nb):
		for i in range(0,na):
			if MissingValue in (PAF[i],PAF[i]):
				N=N+1
			else:
				AVAL=AVAL+PAF[i]*PAV[i]
				SUM=SUM+PAF[i]
		if(SUM==0):
			AVAL=MissingValue
		else:
			AVAL=(AVAL/SUM)
	else:
		AVAL=MissingValue
	return AVAL


def fSigConnectivityModel(FA,CA):
	"""
	Inputs:
	1.  FA Matrix: Volume fractions of each component
	2.  CA Matrix: Conductivity values associated with each matrix component
	Outputs:
	1. 	Sigma: Conductivity of the system calculated using the CRI Mixing Law
	"""
	na=len(FA)
	nb=len(CA)
	Sigma=0
	if(na==nb):
		for i in range(0,na):
			Sigma=Sigma+FA[i]*(CA[i]**0.5)
		Sigma=(Sigma**2)
	else:
		Sigma=MissingValue
	return Sigma

#
# 5. FORMATION VOLUMETRIC PROPERTIES:
#====================================
#
# 5.1 Alfred & Vernick Model:
#============================
def fAVM(RHOB,Dw,Ds,Df,Dc1,PHIc1,Ck,Dk,PHIk,RSK):	
	"""
	This procedure operates in a manner analogues to the Alfred and Venick Model.	
	Inputs:
	1.	RHOB	Bulk Density (g/cm3)
	2.	Dw		Density for formation water (g/cm3)
	3.	Ds		Density for adsorbed (sorbed) hydrocarbon (g/cm3)
	4.	Df		Density for free hydrocarbon (g/cm3)
	5.	Dc1		Density for component 1 (g/cm3)
	6.	PHIc1	Microporosity for component 1 (frac)
	7.	Ck		Wt Organic carbon divided by Wt of kerogen
	8.	Dk		Density for kerogen (g/cm3)
	9.	PHIk	Porosity for kerogen (frac)
	10.	RSK		Ratio of adsorbed (sorbed) hydrocarbon volume to kerogen volume (i.e. Fs/Fk).
	Outputs:
	1. 	PHIt:	Total Porosity (frac)
	2. 	PHIe: 	Effective Porosity (frac)
	3. 	CBW: 	Clay Bound Water (Microporosity) (frac)
	4. 	BVW: 	Bulk volume of water (frac)
	5.  HCPV:	Hydrocarbon pore volume (frac)
	5.	Vf: 	Free Hydrocarbon pore volume (frac)
	6. 	Vs: 	Adsorbed (Sorbed) Hydrocarbon pore volume (frac)
	7.	SWt: 	Total Water Saturation (frac)
	9.	SWe: 	Effective Water Saturation (frac)
	10.	Vc1: 	Component 2 volume (frac)
	11. Vc2: 	Component 2 Volume (frac)
	12. Vc3: 	Component 3 Volume (frac)
	13. Vk:		Kerogen volume (frac)
	14. Toc:	Total Organic Carbon (wt%)
	15.	Qc: 	Quality Control Flag
	16.	GDen:	Grain Density (g/cm3)
	"""
#
#   5.1.1 Initialise Outputs & Check for missing values in inputs:
#   --------------------------------------------------------------
	PHIt=MissingValue
	PHIe=MissingValue
	CBW=MissingValue
	BVW=MissingValue
	HCPV=MissingValue
	Vf=MissingValue
	Vs=MissingValue
	Swt=MissingValue
	Swe=MissingValue
	Vc1=MissingValue
	Vc2=MissingValue
	Vc3=MissingValue
	Vk=MissingValue
	Toc=MissingValue
	Qc=MissingValue
	GDen=MissingValue
	if MissingValue in (RHOB,Dw,Ds,Df,Dc1,PHIc1,Ck,Dk,PHIk,RSK):
		return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#   5.1.2 Initialise parameters:
#   ----------------------------
	NIter=0
	NIterMax=100
	ErrIter=10000
	TolErrIter=0.0001
	IterEnd=0
	Vk=0.000 # Initially assumme no kerogen
	Dh=Df
#
#	5.1.3  Start interative loop:
#	-----------------------------
	while IterEnd==0:
#
#   5.5.3.1 Organic and Inorganic Component Density Values:
#   -------------------------------------------------------
		DBI=(1-PHIc1)*Dc1+(PHIc1*Dw) # Bulk Density of Inorganic Component
		DBO=(1-PHIk)*Dk+(PHIk*Dh)# Bulk Density of Organic Component
#
#   5.1.3.2 Compute Volume of Organic and Inorganic Component:
#   ----------------------------------------------------------
		VOR=(DBI-RHOB)/(DBI-DBO)
		VOR=ImposeLimits(VOR,0,1)
		VIN=(1-VOR)
#
#   5.1.3.3 Compute Volumetrics, Total & Effective Porosity and Total & Effective Water Saturation:
#   ---------------------------------------	-------------------------------------------------------
		Vc1=VIN*(1-PHIc1)
		Vc2=0.000
		Vc3=0.000
		Vk=VOR*(1-PHIk)
		PHIt=VIN*PHIc1+VOR*PHIk
		PHIe=VOR*PHIk
		Swt=1-((VOR*PHIk)/PHIt)
		Swt=ImposeLimits(Swt,0,1)
		Swe=0.000
		Sxot=Swt
		Sxoe=Swe
#
#   5.1.3.4 Compute Bulk Volume of Water, Hydrocarbon Pore Volume and Pore Space Fluid Properties:
#   ---------------------------------------	------------------------------------------------------
		BVW=PHIe*Swe
		HCPV=PHIe*(1-Swe)
		Vs=RSK*Vk # Estimate volume of adsorbed (sorbed) hydrocarbon
		Vs=ImposeLimits(Vs,0,HCPV)
		Vf=(HCPV-Vs)
		Vf=ImposeLimits(Vf,0,(HCPV-Vs))
#
#   5.1.3.5 Recompute hydrocarbon properties in the pore space:
#   -----------------------------------------------------------
		Sum=Vs+Vf
		if(Sum<=0.000):
			Dh=Df
		else:
			Dh=(Ds*Vs+Df*Vf)/(Vs+Vf)
#
#   5.1.4 Test for interative computations:
#   ---------------------------------------
		NIter=NIter+1
		if(NIter>=NIterMax):
			IterEnd=1
		else:			
			if(NIter<=2):
				ResultOld=[1,1,1,1,1,1,1,1,1] # Initial Setting
				ResultNew=[Vc1,Vc2,Vc3,Vk,Vs,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
			else:
				ResultNew=[Vc1,Vc2,Vc3,Vk,Vs,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
				if(ErrIter<=TolErrIter):
					IterEnd=1
#
#   5.1.6  Preoutput computations:
#   ------------------------------
	Qc=MissingValue
	Dc2=0.00
	Dc3=0.00
	CBW=PHIt-PHIe # The assumption is that all microporosity can be considered to be clay bound water.
	Toc=fToc_Wtf(Vc1,Vc2,Vc3,Vk,0,Ck,Dc1,Dc2,Dc3,Dk,Dw) # TOC-wt fraction. Note: Vrw=0 in fToc_Wtf(Vc1,Vc2,Vc3,Vk,Vrw,Ck,Dc1,Dc2,Dc3,Dk,Dw)
	GDen=fOrmGDen(Vc1,Vc2,Vc3,Vk,0,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density. Note: Vrw=0 in fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw)
#
#   5.5.7 Output Results:
#  	-------------------
	return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
# 5.1 Single Matrix Component & Kerogen Resistivity Model:
#=========================================================
def ORM1(RHOB,PHIN,DTCO,RD,Dw,HIw,DTw,Rw,Df,HIf,DTf,Rf,Da,HIa,DTa,Ra,Dc1,HIc1,DTc1,PHIc1,Rc1,Dc2,HIc2,DTc2,PHIc2,Rc2,Dc3,HIc3,DTc3,PHIc3,Rc3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Cwv,Ckv,Alpha,Sxoe):	
	"""
	This procedure uses Density, Neutron, Compressional Slowness and Resistivity data to compute volumes of components 1 and 2, kerogen and effective porosity.
	The model assumes that all organic porosity is only hydrocarbon bearing, but it allows for the presence of free hydrocarbons and water in the inorganic porosity.
	Inputs:
	1.	RHOB	Bulk Density (g/cm3)
	2.	PHIN	Neutron Porosity (frac)
	3.	DTCO 	Compressional Slowness (us/ft)
	4.	RD		Resistivity (Ohm.m)
	5.	Dw		Density for formation water (g/cm3)
	6.	Hw		Hydrogen index for formation water (frac)
	7.	DTw		Compressional Slowness for formation water (us/ft)
	8.	Rw		Formation water resistivity (Ohm.m)
	9.	Da		Density for adsorbed (sorbed) hydrocarbon (g/cm3)
	10.	Ha		Hydrogen index for adsorbed (sorbed) hydrocarbon (frac)
	11.	DTa		Compressional Slowness for adsorbed (sorbed) hydrocarbon (us/ft)
	12.	Ra		Resistivity for adsorbed (sorbed) hydrocarbon (Ohm.m)
	13.	Df		Density for free hydrocarbon (g/cm3)
	14.	Hf		Hydrogen index for free hydrocarbon (frac)
	15.	DTf		Compressional Slowness for free hydrocarbon (us/ft)
	16.	Rf		Resistivity for free hydrocarbon (Ohm.m)
	17. Dc1		Density for component 1 (g/cm3)
	18.	HIc1	Hydrogen index for component 1 (frac)
	19.	DTc1	Compressional Slowness for component 1 (us/ft)
	20.	PHIc1	Microporosity for component 1 (frac)
	21.	Rc1		Resistivity for component 1 (Ohm.m)
	22. Dc2		Density for component 2 (g/cm3)
	23.	HIc2	Hydrogen index for component 2 (frac)
	24.	DTc2	Compressional Slowness for component 2 (us/ft)
	25.	PHIc2	Microporosity for component 2 (frac)
	26.	Rc2		Resistivity for component 2 (Ohm.m)
	27. Dc3		Density for component 3 (g/cm3)
	28.	HIc3	Hydrogen index for component 3 (frac)
	29.	DTc3	Compressional Slowness for component 3 (us/ft)
	30.	PHIc3	Microporosity for component 3 (frac)
	31.	Rc3		Resistivity for component 3 (Ohm.m)
	32.	Ck		Wt Organic carbon divided by Wt of kerogen
	33.	Dk		Density for kerogen (g/cm3)
	34.	HIk		Hydrogen index for kerogen (frac)
	35.	DTk		Compressional Slowness for kerogen (us/ft)
	36.	PHIk	Porosity for kerogen (frac)
	37.	Rk		Resistivity for kerogen (Ohm.m).
	38.	RSK		Ratio of adsorbed (sorbed) hydrocarbon volume to kerogen volume (i.e. Fs/Fk).
	39. Cwv		Critical Water Volume (frac)
	40.	Ckv		Critical Kerogen Volume (frac)
	41. Alpha	Factor used on the Monteron (CRIM) Connectivity Theory Resistivity Model (Default value = 2.0)	
	42. Sxoe	Near Wellbore Invastion Parameter
#
	Outputs:
	1. 	PHIt:	Total Porosity (frac)
	2. 	PHIe: 	Effective Porosity (frac)
	3. 	CBW: 	Clay Bound Water (Microporosity) (frac)
	4. 	BVW: 	Bulk volume of water (frac)
	5.  HCPV:	Hydrocarbon pore volume (frac)
	5.	Vf: 	Free Hydrocarbon pore volume (frac)
	6. 	Vs: 	Adsorbed (Sorbed) Hydrocarbon pore volume (frac)
	7.	SWt: 	Total Water Saturation (frac)
	9.	SWe: 	Effective Water Saturation (frac)
	12.	Vc1: 	Component 2 volume (frac)
	13. Vc2: 	Component 2 Volume (frac)
	14. Vc3: 	Component 3 Volume (frac)
	15. Vk:		Kerogen volume (frac)
	16. Toc:	Total Organic Carbon (wt%)
	17.	Qc: 	Quality Control Flag
	18.	GDen:	Grain Density (g/cm3)
	"""
#
#   5.1.1 Initialise Outputs & Check for missing values in inputs:
#   --------------------------------------------------------------
	PHIt=MissingValue
	PHIe=MissingValue
	CBW=MissingValue
	BVW=MissingValue
	HCPV=MissingValue
	Vf=MissingValue
	Vs=MissingValue
	Swt=MissingValue
	Swe=MissingValue
	Vc1=MissingValue
	Vc2=MissingValue
	Vc3=MissingValue
	Vk=MissingValue
	Toc=MissingValue
	Qc=MissingValue
	GDen=MissingValue
	if MissingValue in (RHOB,PHIN,DTCO,RD,Dw,HIw,DTw,Rw,Df,HIf,DTf,Rf,Da,HIa,DTa,Ra,Dc1,HIc1,DTc1,PHIc1,Rc1,Dc2,HIc2,DTc2,PHIc2,Rc2,Dc3,HIc3,DTc3,PHIc3,Rc3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Cwv,Ckv,Alpha,Sxoe):
		return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#   5.1.2 Initialise parameters:
#   ----------------------------
#	5.1.2.1 Initialise Interation Control Paramaeters:
#	--------------------------------------------------
	NIter=0
	NIterMax=100
	ErrIter=10000
	TolErrIter=0.0001
	IterEnd=0
#
#	5.1.2.2 Initialise Volumes and Hydrocarbon Properties:
#	------------------------------------------------------
	Vk=0.000 # Volume of kerogen initialised to zero
	Va=0.000 # Volume of adsorbed gas initialised to zero
	Vf=0.000 # Volume of free gas initialised to zero
#
#	5.7.3  Start interative loop:
#	-----------------------------
	while IterEnd==0:
#
#   5.7.3.1 Compute Pore Fluid Properties:
#   --------------------------------------
		Sum=Va+Vf
		if(Sum==0):
			Dh=Df
			HIh=HIf
			DTh=DTf
		else:
			Dh=(Va*Da+Vf*Df)/Sum
			HIh=(Va*HIa+Vf*HIf)/Sum
			DTh=(Va*DTa+Vf*DTf)/Sum
		Dpf=(Sxoe*Dw)+(1-Sxoe)*Dh # Density of pore fluid
		HIpf=(Sxoe*HIw)+(1-Sxoe)*HIh # Hydrogen Index of pore fluid
		DTpf=(Sxoe*DTw)+(1-Sxoe)*DTh # DT of pore fluid	
#
#	5.7.3.2 Matrix Inversion:
#	-------------------------
		YMatrix = [RHOB,PHIN,DTCO,1] # Populate YMatrix
		AMatrix = [[Dc1,Dc2,Dk,Dpf],[HIc1,HIc2,HIk,HIpf],[DTc1,DTc2,DTk,DTpf],[1,1,1,1]] # Populate AMatrix
		XMatrix,Qc=SolveAndCorrect(AMatrix,YMatrix) # Solve for XMatrix
		Vc1=XMatrix[0] # Volume of component 1
		Vc2=XMatrix[1] # Volume of component 2
		Vc3=0.000 # Volume of component 3 (not calculated in this routine).
		Vk=XMatrix[2] # Volume of organic component
		PHIe=XMatrix[3] # Volume of hydrocarbon in organic and inorganic pores
#
#	5.7.3.3 Determine Total & Effective Water Saturations:
#	-----------------------------------------------------
		PHIm=(Vc1*PHIc1)+(Vc2*PHIc2)+(Vc3*PHIc3) # Compute Micro Porosity
		PHIt=PHIm+PHIe
		Swe=fConnectivityModel(RD,Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rf,Cwv,Ckv,Alpha)
		if(PHIt==0):
			Swt=1.000
		else:
			Swt=(PHIm+PHIe*Swe)/PHIt
#
#	5.7.4.3 Compute Volume of Adsorbed and Free Gas:
#	------------------------------------------------
		Va=RSK*Vk # Volume of adsorbed gas in organic pores
		HCPV=PHIt*(1-Swt)
		if(Va>=HCPV):
			Va=HCPV
		Vf=HCPV-Va # Volume of free gas	
#
#   5.4.4 Test for interative computations:
#   ---------------------------------------
		NIter=NIter+1
		if(NIter>=NIterMax):
			IterEnd=1
		else:			
			if(NIter<=2):
				ResultOld=[1,1,1,1,1,1,1,1,1] # Initial Setting
				ResultNew=[Vc1,Vc2,Vc3,Vk,Va,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
			else:
				ResultNew=[Vc1,Vc2,Vc3,Vk,Va,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
				if(ErrIter<=TolErrIter):
					IterEnd=1
#
#   5.4.6  Preoutput computations:
#   ------------------------------
	CBW=PHIm # The assumption is that all microporosity can be considered to be clay bound water.
	BVW=PHIe*Swe # Bulk volume of water
	HCPV=PHIt*(1-Swt) # Hydrocarbon pore volume	
	Toc=fToc_Wtf(Vc1,Vc2,Vc3,Vk,0,Ck,Dc1,Dc2,Dc3,Dk,Dw) # TOC-wt fraction. Note: Vrw=0 in fToc_Wtf(Vc1,Vc2,Vc3,Vk,Vrw,Ck,Dc1,Dc2,Dc3,Dk,Dw) # Total Organic Carbon wt%
	GDen=fOrmGDen(Vc1,Vc2,Vc3,Vk,0,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density. Note: Vrw=0 in fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density g/cm3
#
#   5.4.7 Output Results:
#  	-------------------
	return PHIt,PHIe,CBW,BVW,HCPV,Vf,Va,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
# 5.2 Single Matrix Component & Kerogen Resistivity Model:
#=========================================================
def ORM2(RHOB,PHIN,DTCO,RD,Dw,HIw,DTw,Rw,Df,HIf,DTf,Rf,Da,HIa,DTa,Ra,Dc1,HIc1,DTc1,PHIc1,Rc1,Dc2,HIc2,DTc2,PHIc2,Rc2,Dc3,HIc3,DTc3,PHIc3,Rc3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Cwv,Ckv,Alpha,Sxoe):	
	"""
	This procedure uses Density, Neutron and Resistivity data to compute volumes of components 1 kerogen and effective porosity.
	Inputs:
	1.	RHOB	Bulk Density (g/cm3)
	2.	PHIN	Neutron Porosity (frac)
	3.	DTCO 	Compressional Slowness (us/ft)
	4.	RD		Resistivity (Ohm.m)
	5.	Dw		Density for formation water (g/cm3)
	6.	Hw		Hydrogen index for formation water (frac)
	7.	DTw		Compressional Slowness for formation water (us/ft)
	8.	Rw		Formation water resistivity (Ohm.m)
	9.	Da		Density for adsorbed (sorbed) hydrocarbon (g/cm3)
	10.	Ha		Hydrogen index for adsorbed (sorbed) hydrocarbon (frac)
	11.	DTa		Compressional Slowness for adsorbed (sorbed) hydrocarbon (us/ft)
	12.	Ra		Resistivity for adsorbed (sorbed) hydrocarbon (Ohm.m)
	13.	Df		Density for free hydrocarbon (g/cm3)
	14.	Hf		Hydrogen index for free hydrocarbon (frac)
	15.	DTf		Compressional Slowness for free hydrocarbon (us/ft)
	16.	Rf		Resistivity for free hydrocarbon (Ohm.m)
	17. Dc1		Density for component 1 (g/cm3)
	18.	HIc1	Hydrogen index for component 1 (frac)
	19.	DTc1	Compressional Slowness for component 1 (us/ft)
	20.	PHIc1	Microporosity for component 1 (frac)
	21.	Rc1		Resistivity for component 1 (Ohm.m)
	22. Dc2		Density for component 2 (g/cm3)
	23.	HIc2	Hydrogen index for component 2 (frac)
	24.	DTc2	Compressional Slowness for component 2 (us/ft)
	25.	PHIc2	Microporosity for component 2 (frac)
	26.	Rc2		Resistivity for component 2 (Ohm.m)
	27. Dc3		Density for component 3 (g/cm3)
	28.	HIc3	Hydrogen index for component 3 (frac)
	29.	DTc3	Compressional Slowness for component 3 (us/ft)
	30.	PHIc3	Microporosity for component 3 (frac)
	31.	Rc3		Resistivity for component 3 (Ohm.m)
	32.	Ck		Wt Organic carbon divided by Wt of kerogen
	33.	Dk		Density for kerogen (g/cm3)
	34.	HIk		Hydrogen index for kerogen (frac)
	35.	DTk		Compressional Slowness for kerogen (us/ft)
	36.	PHIk	Porosity for kerogen (frac)
	37.	Rk		Resistivity for kerogen (Ohm.m).
	38.	RSK		Ratio of adsorbed (sorbed) hydrocarbon volume to kerogen volume (i.e. Fs/Fk).
	39. Cwv		Critical Water Volume (frac)
	40.	Ckv		Critical Kerogen Volume (frac)
	41. Alpha	Factor used on the Monteron (CRIM) Connectivity Theory Resistivity Model (Default value = 2.0)	
	42. Sxoe	Near Wellbore Invastion Parameter
#
	Outputs:
	1. 	PHIt:	Total Porosity (frac)
	2. 	PHIe: 	Effective Porosity (frac)
	3. 	CBW: 	Clay Bound Water (Microporosity) (frac)
	4. 	BVW: 	Bulk volume of water (frac)
	5.  HCPV:	Hydrocarbon pore volume (frac)
	5.	Vf: 	Free Hydrocarbon pore volume (frac)
	6. 	Vs: 	Adsorbed (Sorbed) Hydrocarbon pore volume (frac)
	7.	SWt: 	Total Water Saturation (frac)
	9.	SWe: 	Effective Water Saturation (frac)
	12.	Vc1: 	Component 2 volume (frac)
	13. Vc2: 	Component 2 Volume (frac)
	14. Vc3: 	Component 3 Volume (frac)
	15. Vk:		Kerogen volume (frac)
	16. Toc:	Total Organic Carbon (wt%)
	17.	Qc: 	Quality Control Flag
	18.	GDen:	Grain Density (g/cm3)
	"""
#
#   5.1.1 Initialise Outputs & Check for missing values in inputs:
#   --------------------------------------------------------------
	PHIt=MissingValue
	PHIe=MissingValue
	CBW=MissingValue
	BVW=MissingValue
	HCPV=MissingValue
	Vf=MissingValue
	Vs=MissingValue
	Swt=MissingValue
	Swe=MissingValue
	Vc1=MissingValue
	Vc2=MissingValue
	Vc3=MissingValue
	Vk=MissingValue
	Toc=MissingValue
	Qc=MissingValue
	GDen=MissingValue
	if MissingValue in (RHOB,PHIN,DTCO,RD,Dw,HIw,DTw,Rw,Df,HIf,DTf,Rf,Da,HIa,DTa,Ra,Dc1,HIc1,DTc1,PHIc1,Rc1,Dc2,HIc2,DTc2,PHIc2,Rc2,Dc3,HIc3,DTc3,PHIc3,Rc3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Cwv,Ckv,Alpha,Sxoe):
		return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#   5.1.2 Initialise parameters:
#   ----------------------------
#	5.1.2.1 Initialise Interation Control Paramaeters:
#	--------------------------------------------------
	NIter=0
	NIterMax=100
	ErrIter=10000
	TolErrIter=0.0001
	IterEnd=0
#
#	5.1.2.2 Initialise Volumes and Hydrocarbon Properties:
#	------------------------------------------------------
	Vk=0.000 # Volume of kerogen initialised to zero
	Va=0.000 # Volume of adsorbed gas initialised to zero
	Vf=0.000 # Volume of free gas initialised to zero
#
#	5.7.3  Start interative loop:
#	-----------------------------
	while IterEnd==0:
#
#   5.7.3.1 Compute Pore Fluid Properties:
#   --------------------------------------
		Sum=Va+Vf
		if(Sum==0):
			Dh=Df
			HIh=HIf
			DTh=DTf
		else:
			Dh=(Va*Da+Vf*Df)/Sum
			HIh=(Va*HIa+Vf*HIf)/Sum
			DTh=(Va*DTa+Vf*DTf)/Sum
		Dpf=(Sxoe*Dw)+(1-Sxoe)*Dh # Density of pore fluid
		HIpf=(Sxoe*HIw)+(1-Sxoe)*HIh # Hydrogen Index of pore fluid
		DTpf=(Sxoe*DTw)+(1-Sxoe)*DTh # DT of pore fluid	
#
#	5.7.3.2 Matrix Inversion:
#	-------------------------
		YMatrix = [RHOB,PHIN,1] # Populate YMatrix
		AMatrix = [[Dc1,Dk,Dpf],[HIc1,HIk,HIpf],[1,1,1]] # Populate AMatrix
		XMatrix,Qc=SolveAndCorrect(AMatrix,YMatrix) # Solve for XMatrix
		Vc1=XMatrix[0] # Volume of component 1
		Vc2=0.000 # Volume of component 2
		Vc3=0.000 # Volume of component 3 (not calculated in this routine).
		Vk=XMatrix[1] # Volume of organic component
		PHIe=XMatrix[2] # Volume of hydrocarbon in organic and inorganic pores
#
#	5.7.3.3 Determine Total & Effective Water Saturations:
#	-----------------------------------------------------
		PHIm=(Vc1*PHIc1)+(Vc2*PHIc2)+(Vc3*PHIc3) # Compute Micro Porosity
		PHIt=PHIm+PHIe
		Swe=fConnectivityModel(RD,Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rf,Cwv,Ckv,Alpha)
		if(PHIt==0):
			Swt=1.000
		else:
			Swt=(PHIm+PHIe*Swe)/PHIt
#
#	5.7.4.3 Compute Volume of Adsorbed and Free Gas:
#	------------------------------------------------
		Va=RSK*Vk # Volume of adsorbed gas in organic pores
		HCPV=PHIt*(1-Swt)
		if(Va>=HCPV):
			Va=HCPV
		Vf=HCPV-Va # Volume of free gas	
#
#   5.4.4 Test for interative computations:
#   ---------------------------------------
		NIter=NIter+1
		if(NIter>=NIterMax):
			IterEnd=1
		else:			
			if(NIter<=2):
				ResultOld=[1,1,1,1,1,1,1,1,1] # Initial Setting
				ResultNew=[Vc1,Vc2,Vc3,Vk,Va,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
			else:
				ResultNew=[Vc1,Vc2,Vc3,Vk,Va,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
				if(ErrIter<=TolErrIter):
					IterEnd=1
#
#   5.4.6  Preoutput computations:
#   ------------------------------
	CBW=PHIm # The assumption is that all microporosity can be considered to be clay bound water.
	BVW=PHIe*Swe # Bulk volume of water
	HCPV=PHIt*(1-Swt) # Hydrocarbon pore volume	
	Toc=fToc_Wtf(Vc1,Vc2,Vc3,Vk,0,Ck,Dc1,Dc2,Dc3,Dk,Dw) # TOC-wt fraction. Note: Vrw=0 in fToc_Wtf(Vc1,Vc2,Vc3,Vk,Vrw,Ck,Dc1,Dc2,Dc3,Dk,Dw) # Total Organic Carbon wt%
	GDen=fOrmGDen(Vc1,Vc2,Vc3,Vk,0,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density. Note: Vrw=0 in fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density g/cm3
#
#   5.4.7 Output Results:
#  	-------------------
	return PHIt,PHIe,CBW,BVW,HCPV,Vf,Va,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
# 5.3 Two Component & Kerogen Resistivity Model:
#=========================================================
def ORM3(GR,RHOB,PHIN,RD,DTCO,Dw,HIw,Gw,Rw,DTw,Df,HIf,Gf,Rf,DTf,Da,HIa,Ga,Ra,DTa,Dc1,HIc1,Gc1,PHIc1,Rc1,DTc1,Dc2,HIc2,Gc2,PHIc2,Rc2,DTc2,Dc3,HIc3,Gc3,PHIc3,Rc3,DTc3,Ck,Dk,HIk,Gk,PHIk,Rk,DTk,RSK,Cwv,Ckv,Alpha,Sxoe):	
	"""
	This procedure uses Gamma Ray, Density, Neutron and Resistivity data to compute volumes of components 1 and 2, kerogen and effective porosity.
	Inputs:
	1.	GR		Gamma Ray (API)
	2.	RHOB	Bulk Density (g/cm3)
	3.	PHIN	Neutron Porosity (frac)
	4.	RD		Resistivity (Ohm.m)
	5.	Dw		Density for formation water (g/cm3)
	6.	Hw		Hydrogen index for formation water (frac)
	7.	Gw		Gamma Ray for formation water (us/ft)
	8.	Rw		Formation water resistivity (Ohm.m)
	9.	Da		Density for adsorbed (sorbed) hydrocarbon (g/cm3)
	10.	Ha		Hydrogen index for adsorbed (sorbed) hydrocarbon (frac)
	11.	Ga		Gamma Ray for adsorbed (sorbed) hydrocarbon (us/ft)
	12.	Ra		Resistivity for adsorbed (sorbed) hydrocarbon (Ohm.m)
	13.	Df		Density for free hydrocarbon (g/cm3)
	14.	Hf		Hydrogen index for free hydrocarbon (frac)
	15.	Gf		Gamma Ray for free hydrocarbon (us/ft)
	16.	Rf		Resistivity for free hydrocarbon (Ohm.m)
	17. Dc1		Density for component 1 (g/cm3)
	18.	HIc1	Hydrogen index for component 1 (frac)
	19.	Gc1		Gamma Ray for component 1 (us/ft)
	20.	PHIc1	Microporosity for component 1 (frac)
	21.	Rc1		Resistivity for component 1 (Ohm.m)
	22. Dc2		Density for component 2 (g/cm3)
	23.	HIc2	Hydrogen index for component 2 (frac)
	24.	Gc2		Gamma Ray for component 2 (us/ft)
	25.	PHIc2	Microporosity for component 2 (frac)
	26.	Rc2		Resistivity for component 2 (Ohm.m)
	27. Dc3		Density for component 3 (g/cm3)
	28.	HIc3	Hydrogen index for component 3 (frac)
	29.	Gc3		Gamma Ray for component 3 (us/ft)
	30.	PHIc3	Microporosity for component 3 (frac)
	31.	Rc3		Resistivity for component 3 (Ohm.m)
	32.	Ck		Wt Organic carbon divided by Wt of kerogen
	33.	Dk		Density for kerogen (g/cm3)
	34.	HIk		Hydrogen index for kerogen (frac)
	35.	Gk		Gamma Ray for kerogen (us/ft)
	36.	PHIk	Porosity for kerogen (frac)
	37.	Rk		Resistivity for kerogen (Ohm.m).
	38.	RSK		Ratio of adsorbed (sorbed) hydrocarbon volume to kerogen volume (i.e. Fs/Fk).
	39. Cwv		Critical Water Volume (frac)
	40.	Ckv		Critical Kerogen Volume (frac)
	41. Alpha	Factor used on the Monteron (CRIM) Connectivity Theory Resistivity Model (Default value = 2.0)	
	42. Sxoe	Near Wellbore Invastion Parameter
#
	Outputs:
	1. 	PHIt:	Total Porosity (frac)
	2. 	PHIe: 	Effective Porosity (frac)
	3. 	CBW: 	Clay Bound Water (Microporosity) (frac)
	4. 	BVW: 	Bulk volume of water (frac)
	5.  HCPV:	Hydrocarbon pore volume (frac)
	5.	Vf: 	Free Hydrocarbon pore volume (frac)
	6. 	Vs: 	Adsorbed (Sorbed) Hydrocarbon pore volume (frac)
	7.	SWt: 	Total Water Saturation (frac)
	9.	SWe: 	Effective Water Saturation (frac)
	12.	Vc1: 	Component 2 volume (frac)
	13. Vc2: 	Component 2 Volume (frac)
	14. Vc3: 	Component 3 Volume (frac)
	15. Vk:		Kerogen volume (frac)
	16. Toc:	Total Organic Carbon (wt%)
	17.	Qc: 	Quality Control Flag
	18.	GDen:	Grain Density (g/cm3)
	"""
#
#   5.1.1 Initialise Outputs & Check for missing values in inputs:
#   --------------------------------------------------------------
	PHIt=MissingValue
	PHIe=MissingValue
	CBW=MissingValue
	BVW=MissingValue
	HCPV=MissingValue
	Vf=MissingValue
	Vs=MissingValue
	Swt=MissingValue
	Swe=MissingValue
	Vc1=MissingValue
	Vc2=MissingValue
	Vc3=MissingValue
	Vk=MissingValue
	Toc=MissingValue
	Qc=MissingValue
	GDen=MissingValue
	if MissingValue in (GR,RHOB,PHIN,RD,DTCO,Dw,HIw,Gw,Rw,DTw,Df,HIf,Gf,Rf,DTf,Da,HIa,Ga,Ra,DTa,Dc1,HIc1,Gc1,PHIc1,Rc1,DTc1,Dc2,HIc2,Gc2,PHIc2,Rc2,DTc2,Dc3,HIc3,Gc3,PHIc3,Rc3,DTc3,Ck,Dk,HIk,Gk,PHIk,Rk,DTk,RSK,Cwv,Ckv,Alpha,Sxoe):
		return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#   5.1.2 Initialise parameters:
#   ----------------------------
#	5.1.2.1 Initialise Interation Control Paramaeters:
#	--------------------------------------------------
	NIter=0
	NIterMax=100
	ErrIter=10000
	TolErrIter=0.0001
	IterEnd=0
#
#	5.1.2.2 Initialise Volumes and Hydrocarbon Properties:
#	------------------------------------------------------
	Vk=0.000 # Volume of kerogen initialised to zero
	Va=0.000 # Volume of adsorbed gas initialised to zero
	Vf=0.000 # Volume of free gas initialised to zero
#
#	5.7.3  Start interative loop:
#	-----------------------------
	while IterEnd==0:
#
#   5.7.3.1 Compute Pore Fluid Properties:
#   --------------------------------------
		Sum=Va+Vf
		if(Sum==0):
			Dh=Df
			HIh=HIf
			Gh=Gf
			DTh=DTf
		else:
			Dh=(Va*Da+Vf*Df)/Sum
			HIh=(Va*HIa+Vf*HIf)/Sum
			Gh=(Va*Ga+Vf*Gf)/Sum
			DTh=(Va*DTa+Vf*DTf)/Sum
		Dpf=(Sxoe*Dw)+(1-Sxoe)*Dh # Density of pore fluid
		HIpf=(Sxoe*HIw)+(1-Sxoe)*HIh # Hydrogen Index of pore fluid
		Gpf=(Sxoe*Gw)+(1-Sxoe)*Gh # GR of pore fluid
		DTpf=(Sxoe*DTw)+(1-Sxoe)*DTh # DT of pore fluid
#
#	5.7.3.2 Matrix Inversion:
#	-------------------------
		YMatrix = [RHOB,PHIN,GR,DTCO,1] # Populate YMatrix
		AMatrix = [[Dc1,Dc2,Dc3,Dk,Dpf],[HIc1,HIc2,HIc3,HIk,HIpf],[Gc1,Gc2,Gc3,Gk,Gpf],[DTc1,DTc2,DTc3,DTk,DTpf],[1,1,1,1,1]] # Populate AMatrix
		XMatrix,Qc=SolveAndCorrect(AMatrix,YMatrix) # Solve for XMatrix
		Vc1=XMatrix[0] # Volume of component 1
		Vc2=XMatrix[1] # Volume of component 2
		Vc3=XMatrix[2] # Volume of component 3
		Vk=XMatrix[3] # Volume of organic component
		PHIe=XMatrix[4] # Volume of hydrocarbon in organic and inorganic pores
#
#	5.7.3.3 Determine Total & Effective Water Saturations:
#	-----------------------------------------------------
		PHIm=(Vc1*PHIc1)+(Vc2*PHIc2)+(Vc3*PHIc3) # Compute Micro Porosity
		PHIt=PHIm+PHIe
		Swe=fConnectivityModel(RD,Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rf,Cwv,Ckv,Alpha)
		if(PHIt==0):
			Swt=1.000
		else:
			Swt=(PHIm+PHIe*Swe)/PHIt
#
#	5.7.4.3 Compute Volume of Adsorbed and Free Gas:
#	------------------------------------------------
		Va=RSK*Vk # Volume of adsorbed gas in organic pores
		HCPV=PHIt*(1-Swt)
		if(Va>=HCPV):
			Va=HCPV
		Vf=HCPV-Va # Volume of free gas	
#
#   5.4.4 Test for interative computations:
#   ---------------------------------------
		NIter=NIter+1
		if(NIter>=NIterMax):
			IterEnd=1
		else:			
			if(NIter<=2):
				ResultOld=[1,1,1,1,1,1,1,1,1] # Initial Setting
				ResultNew=[Vc1,Vc2,Vc3,Vk,Va,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
			else:
				ResultNew=[Vc1,Vc2,Vc3,Vk,Va,Vf,PHIe,Swt,Swe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
				if(ErrIter<=TolErrIter):
					IterEnd=1
#
#   5.4.6  Preoutput computations:
#   ------------------------------
	CBW=PHIm # The assumption is that all microporosity can be considered to be clay bound water.
	BVW=PHIe*Swe # Bulk volume of water
	HCPV=PHIt*(1-Swt) # Hydrocarbon pore volume	
	Toc=fToc_Wtf(Vc1,Vc2,Vc3,Vk,0,Ck,Dc1,Dc2,Dc3,Dk,Dw) # TOC-wt fraction. Note: Vrw=0 in fToc_Wtf(Vc1,Vc2,Vc3,Vk,Vrw,Ck,Dc1,Dc2,Dc3,Dk,Dw) # Total Organic Carbon wt%
	GDen=fOrmGDen(Vc1,Vc2,Vc3,Vk,0,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density. Note: Vrw=0 in fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density g/cm3
#
#   5.4.7 Output Results:
#  	-------------------
	return PHIt,PHIe,CBW,BVW,HCPV,Vf,Va,Swt,Swe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#
# 5.5 Two Component & Kerogen Resistivity Model:
#=========================================================
def ORM4(RHOB,PHIN,DTCO,RS,RD,SxoMod,Afac,ExC,Dw,HIw,DTw,Rw,Rmf,Ds,HIs,DTs,Rs,Df,HIf,DTf,Rf,Dc1,HIc1,DTc1,PHIc1,Rc1,Dc2,HIc2,DTc2,PHIc2,Rc2,Dc3,HIc3,DTc3,PHIc3,Rc3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Alpha):	
	"""
	This procedure uses Density, Neutron, Compressional Slowness and Resistivity data to compute volumes of components 1 and 2, kerogen and effective porosity.
	The model assumes that all organic porosity is only hydrocarbon bearing, but it allows for the presence of free hydrocarbons and water in the inorganic porosity.
	Inputs:
	1.	RHOB	Bulk Density (g/cm3)
	2.	PHIN	Neutron Porosity (frac)
	3.	DTCO 	Compressional Slowness (us/ft)
	4.	RS		Shallow Resistivity (Ohm.m)
	5.	RD		Resistivity (Ohm.m)
	6.	SxoMod: Near Wellbore Invasion Model (String).
	7.	Afac: 	Sxo=Sw**Afac value.
	8.	ExC: 	Excavation Corrections (String, Y/N)
	9.	Dw		Density for formation water (g/cm3)
	10.	Hw		Hydrogen index for formation water (frac)
	11.	DTw		Compressional Slowness for formation water (us/ft)
	12.	Rw		Formation water resistivity (Ohm.m)
	13. Rmf		Mud Filtrate Resistivity (Ohm.m)
	14.	Ds		Density for adsorbed (sorbed) hydrocarbon (g/cm3)
	15.	Hs		Hydrogen index for adsorbed (sorbed) hydrocarbon (frac)
	16.	DTs		Compressional Slowness for adsorbed (sorbed) hydrocarbon (us/ft)
	17.	Rs		Resistivity for adsorbed (sorbed) hydrocarbon (Ohm.m)
	18.	Df		Density for free hydrocarbon (g/cm3)
	19.	Hf		Hydrogen index for free hydrocarbon (frac)
	20.	DTf		Compressional Slowness for free hydrocarbon (us/ft)
	21.	Rf		Resistivity for free hydrocarbon (Ohm.m)
	22. Dc1		Density for component 1 (g/cm3)
	23.	HIc1	Hydrogen index for component 1 (frac)
	24.	DTc1	Compressional Slowness for component 1 (us/ft)
	25.	PHIc1	Microporosity for component 1 (frac)
	26.	Rc1		Resistivity for component 1 (Ohm.m)
	27. Dc2		Density for component 2 (g/cm3)
	28.	HIc2	Hydrogen index for component 2 (frac)
	29.	DTc2	Compressional Slowness for component 2 (us/ft)
	30.	PHIc2	Microporosity for component 2 (frac)
	31.	Rc2		Resistivity for component 2 (Ohm.m)
	32. Dc3		Density for component 3 (g/cm3)
	33.	HIc3	Hydrogen index for component 3 (frac)
	34.	DTc3	Compressional Slowness for component 3 (us/ft)
	35.	PHIc3	Microporosity for component 3 (frac)
	36.	Rc3		Resistivity for component 3 (Ohm.m)
	37.	Ck		Wt Organic carbon divided by Wt of kerogen
	38.	Dk		Density for kerogen (g/cm3)
	39.	HIk		Hydrogen index for kerogen (frac)
	40.	DTk		Compressional Slowness for kerogen (us/ft)
	40.	PHIk	Porosity for kerogen (frac)
	41.	Rk		Resistivity for kerogen (Ohm.m).
	42.	RSK		Ratio of adsorbed (sorbed) hydrocarbon volume to kerogen volume (i.e. Fs/Fk).
	43. Alpha	Factor used on the Monteron (CRIM) Connectivity Theory Resistivity Model (Default value = 2.0)
#
	Outputs:
	1. 	PHIt:	Total Porosity (frac)
	2. 	PHIe: 	Effective Porosity (frac)
	3. 	CBW: 	Clay Bound Water (Microporosity) (frac)
	4. 	BVW: 	Bulk volume of water (frac)
	5.  HCPV:	Hydrocarbon pore volume (frac)
	5.	Vf: 	Free Hydrocarbon pore volume (frac)
	6. 	Vs: 	Adsorbed (Sorbed) Hydrocarbon pore volume (frac)
	7.	SWt: 	Total Water Saturation (frac)
	9.	SWe: 	Effective Water Saturation (frac)
	10.	Sxot: 	Total Invaded Zone Water Saturation (frac)
	11.	Sxoe: 	Effective Invaded Zone Water Saturation (frac)
	12.	Vc1: 	Component 2 volume (frac)
	13. Vc2: 	Component 2 Volume (frac)
	14. Vc3: 	Component 3 Volume (frac)
	15. Vk:		Kerogen volume (frac)
	16. Toc:	Total Organic Carbon (wt%)
	17.	Qc: 	Quality Control Flag
	18.	GDen:	Grain Density (g/cm3)
	"""
#
#   5.5.1 Initialise Outputs & Check for missing values in inputs:
#   --------------------------------------------------------------
	PHIt=MissingValue
	PHIe=MissingValue
	CBW=MissingValue
	BVW=MissingValue
	HCPV=MissingValue
	Vf=MissingValue
	Vs=MissingValue
	Swt=MissingValue
	Swe=MissingValue
	Sxot=MissingValue
	Sxoe=MissingValue
	Vc1=MissingValue
	Vc2=MissingValue
	Vc3=MissingValue
	Vk=MissingValue
	Toc=MissingValue
	Qc=MissingValue
	GDen=MissingValue
	if((RS==MissingValue)or(RS==0.000)):
		RS=RD
	if MissingValue in (RHOB,PHIN,DTCO,RS,RD,SxoMod,Afac,ExC,Dw,HIw,DTw,Rw,Rmf,Ds,HIs,DTs,Rs,Df,HIf,DTf,Rf,Dc1,HIc1,DTc1,PHIc1,Rc1,Dc2,HIc2,DTc2,PHIc2,Rc2,Dc3,HIc3,DTc3,PHIc3,Rc3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Alpha):
		return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Sxot,Sxoe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#   5.5.2 Initialise parameters:
#   ----------------------------
#	5.5.2.1 Initialise Interation Control Paramaeters:
#	--------------------------------------------------
	NIter=0
	NIterMax=100
	ErrIter=10000
	TolErrIter=0.0001
	IterEnd=0
#
#	5.5.2.2 Initialise Inputs:
#	--------------------------
	if(RD==0):
		Sigt=0.000
	else:
		Sigt=(1/RD)**(1/Alpha)
	if(Rc1==0):
		Sig1=0.000
	else:
		Sig1=(1/Rc1)**(1/Alpha)
	if(Rc2==0):
		Sig2=0.000
	else:
		Sig2=(1/Rc2)**(1/Alpha)
	if(Rc3==0):
		Sig3=0.000
	if(Rk==0):
		Sigk=0.000
	else:
		Sigk=(1/Rk)**(1/Alpha)
	if(Rf==0):
		Sigh=0.000
	else:
		Sigh=(1/Rf)**(1/Alpha)
	if(Rw==0):
		Sigw=0.000
	else:
		Sigw=(1/Rw)**(1/Alpha)
#
#	5.5.2.3 Initialise Volumes and Hydrocarbon Properties:
#	------------------------------------------------------
	Cf=0.000
	PHIe=0.000
	Swe=0.000
	Vk=0.000 # Volume of kerogen initialised to zero
	Vs=0.000 # Volume of adsorbed gas initialised to zero
	Vf=0.000 # Volume of free gas initialised to zero
#
#	5.5.3  Start interative loop:
#	-----------------------------
	while IterEnd==0:
#
#   5.5.3.1 Compute Pore Fluid Properties:
#   --------------------------------------
		Sum=Vs+Vf
		if(Sum==0.000):
			Dh=Df
			HIh=HIf
			DTh=DTf
		else:
			Dh=(Vs*Ds+Vf*Df)/Sum
			HIh=(Vs*HIs+Vf*HIf)/Sum
			DTh=(Vs*DTs+Vf*DTf)/Sum
#
#	5.5.4.1 Matrix Inversion:
#	-------------------------
		YMatrix = [RHOB,PHIN+Cf,DTCO,Sigt,1] # Populate YMatrix
		AMatrix = [[Dc1,Dc2,Dk,Dw,Dh],[HIc1,HIc2,HIk,HIw,HIh],[DTc1,DTc2,DTk,DTw,DTh],[Sig1,Sig2,Sigk,Sigw,Sigh],[1,1,1,1,1]] # Populate AMatrix
		XMatrix,Qc=SolveAndCorrect(AMatrix,YMatrix) # Solve for XMatrix
		Vc1=XMatrix[0] # Volume of component 1
		Vc2=XMatrix[1] # Volume of component 2
		Vc3=0.000 # Volume of component 3 (not calculated in this routine).
		Vk=XMatrix[2] # Volume of organic component
		Vw=XMatrix[3] # Volume of water in inorganic pores
		Vh=XMatrix[4] # Volume of hydrocarbon in organic and inorganic pores
#
#	5.5.4.2 Compute Petrophysics Properties:
#	----------------------------------------
		PHIm=(Vc1*PHIc1)+(Vc2*PHIc2)+(Vc3*PHIc3) # Compute Micro Porosity
		PHIe=Vw+Vh
		PHIt=PHIm+PHIe
		if(PHIe==0.000):
			Swe=1.000
		else:
			Swe=Vw/PHIe
			Swe=ImposeLimits(Swe,0,1)
		if(PHIt==0.000):
			Swt=1.000
		else:
			Swt=(PHIm+PHIe*Swe)/PHIt
			Swt=ImposeLimits(Swt,0,1)
		Sxoe=Swe
		Sxot=Swt
#
#	5.5.4.3 Compute Volume of Adsorbed and Free Gas:
#	------------------------------------------------
		Vs=RSK*Vk # Volume of adsorbed gas in organic pores
		HCPV=PHIe*(1-Swe)
		if(Vs>=HCPV):
			Vs=HCPV
		Vf=HCPV-Vs # Volume of free gas	
#
#   5.5.4.4 Perform Excavation Corrections:
#   ---------------------------------------	
		Cf=ExcCorrected(ExC, Dc1, PHIe, HIf)
#
#   5.5.4 Test for interative computations:
#   ---------------------------------------
		NIter=NIter+1
		if(NIter>=NIterMax):
			IterEnd=1
		else:			
			if(NIter<=2):
				ResultOld=[1,1,1,1,1,1,1,1,1,1,1] # Initial Setting
				ResultNew=[Vc1,Vc2,Vc3,Vk,Vs,Vf,PHIe,Swt,Swe,Sxot,Sxoe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
			else:
				ResultNew=[Vc1,Vc2,Vc3,Vk,Vs,Vf,PHIe,Swt,Swe,Sxot,Sxoe] # Current Results
				ErrIter=ComputeMatrixDifference(ResultOld,ResultNew)
				ResultOld=ResultNew
				if(ErrIter<=TolErrIter):
					IterEnd=1
#
#   5.5.6  Preoutput computations:
#   ------------------------------
	CBW=PHIm # The assumption is that all microporosity can be considered to be clay bound water.
	BVW=PHIe*Swe # Bulk volume of water
	HCPV=PHIt*(1-Swt) # Hydrocarbon pore volume	
	Toc=fToc_Wtf(Vc1,Vc2,Vc3,Vk,0,Ck,Dc1,Dc2,Dc3,Dk,Dw) # TOC-wt fraction. Note: Vrw=0 in fToc_Wtf(Vc1,Vc2,Vc3,Vk,Vrw,Ck,Dc1,Dc2,Dc3,Dk,Dw) # Total Organic Carbon wt%
	GDen=fOrmGDen(Vc1,Vc2,Vc3,Vk,0,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density. Note: Vrw=0 in fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw) # Grain Density g/cm3
#
#   5.5.7 Output Results:
#  	-------------------
	return PHIt,PHIe,CBW,BVW,HCPV,Vf,Vs,Swt,Swe,Sxot,Sxoe,Vc1,Vc2,Vc3,Vk,Toc,Qc,GDen
#
#
# 6. WATER & HYDROCARBON SATURATION PROPERTIES:
#==============================================
#
# 6.1 DUAL WATER MODEL.
#======================
def fDualWater(Ct,PHIt,PHIe,Cfw,Cbw,A,M,N):
	"""
	Inputs:
	1. Ct:   Measured Conductivity
	2. PHIt: Total porosity
	3. PHIe: Effective porosity
	4. Cfw:  Conductivity of free water
	5. Cbw:  Conductivity of bound water
	6. A:    Lithology constant
	7. M:    Porosity exponent
	8. N:    Saturation exponent
	Outputs:
	1. Sw:   Total water saturation.
	"""
#	1. Initialisations:
#	-------------------
	FSwEnd = 0
	FSwInt = 0
	FSwMax = 200
	FSwErr = 0.0001
	SwOld = 1
	SwNew = 1
	SwInc = 0
	Tiny=0.000000001
#
# 2. Interative Loop:
#--------------------
	Swb=((PHIt-PHIe)/PHIt) # Calculate total bound water saturation
	Swb=ImposeLimits(Swb,Tiny,1)
	SwOld=1.000
	while(FSwEnd==0):
		Cm=((PHIt**M)/A)*(SwOld**N)*Cfw+((PHIt**M)/A)*((SwOld**(N-1))*Swb*(Cbw-Cfw))
		r=Ct-Cm
		s=((PHIt**M)/A)*N*(SwOld**(N-1))*Cfw+((PHIt**M)/A)*(N-1)*((SwOld**(N-2))*Swb*(Cbw-Cfw)) # dCm/dSw
		SwInc=(r/s)
		SwNew=SwOld+SwInc
		FSwInt=FSwInt+1
		if(FSwInt>3):	
			if (FSwInt>=FSwMax):
				FSwEnd=1
			if (abs(SwOld-SwNew)<FSwErr):
				FSwEnd=1
		SwOld = SwNew
		SwOld=ImposeLimits(SwOld,Swb,1)
#		
	return SwOld
#
# 6.2 CONNECTIVITY MODEL.
#========================
def fConnectivityModel(RD,Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rh,Cwv,Ckv,Alpha):
	"""
	Function solves the resistivity model equation to compute the water saturation from an input resistivity value.
	Inputs:
	1.	RD		- 	Observed formation resistivity
	2.	Vc1		-	Volume of component #1
	3.	Vc2		-	Volume of component #2
	4.	Vc3		- 	Volume of component #3
	5.	Vk		-	Volume of kerogen 
	6.	PHIe	- 	Effective Poroisty
	7.	Rc1		- 	Resistivity of component #1
	8.	Rc2		-	Resistivity of component #2
	9.	Rc3		-	Resistivity of component #3
	10. Rk		-	Resistivity of kerogen 
	11. Rw		-	Resistivity of water
	12. Rh		- 	Resistivity of hydrocarbon component. Note: it is assumed that this is the same whether the gas is adsorbed or free.
	13. Cwv		- 	Critical Water Volume
	14.	Ckv		-	Critical Kerogen Volume
	15.	Alpha	-	CRIM Mixing Law Exponent
	Output:
	1.	Swe 	- 	Effective Water Saturation
	"""
#
#   1. Initialisations:
#  	-------------------
	FSwEnd = 0
	FSwInt = 0
	FSwMax = 200
	FSwErr = 0.0001
	SwOld = 1
	SwNew = 1
	SwInc = 0
	Tiny=0.000000001
	Big=1000000000000
	Tout=0 # Defines output of fRCrim
#
# 2. Calculate Observed Conductivity:
#-----------------------------------
	if(RD<=0):
		Ct=Big
	else:
		Ct=1/RD
#
# 2. Interative Loop:
#--------------------		
	SwOld=0.50 # Initialises Effective Water Saturation
	while(FSwEnd==0):
		Cm=fRCrim(SwOld,Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rh,Cwv,Ckv,Alpha,Tout)
		r=Ct-Cm
		s=(Cm-fRCrim((SwOld-Tiny),Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rh,Cwv,Ckv,Alpha,Tout))/Tiny # dCm/dSw
		if(s==0): 
			FSwEnd=1
			s=Tiny
		SwInc=(r/s)
		SwNew=SwOld+SwInc
		FSwInt=FSwInt+1
		if(FSwInt>3):	
			if (FSwInt>=FSwMax):
				FSwEnd=1
			if (abs(SwOld-SwNew)<FSwErr):
				FSwEnd=1
		SwOld=SwNew
		SwOld=ImposeLimits(SwOld,Tiny,1)
	#		
	return SwOld
#
# 7. KEROGEN PROPERTIES MODEL:
#=============================
def KPMO(XVal,YVal_State_1,YVal_State_2,YVal_State_3,XVal_Mean_Trans_1,XVal_Mean_Trans_2,XVal_Sig_Trans_1,XVal_Sig_Trans_2,iOpt):
	"""
	This calculates the value of a property YVal based on a measure of Kerogen maturity (XVal).
	The Kerogen maturity model assumes that there are two processes taking place as Kerogen matures from an initial state (State 1) via an intermediate
	state (State 2), to a final state (State 3), depending on some measure of the maturity of the Kerogen (XVal).
	With respect to the Kerogen two transitions are considered to occur:
	The first transition is associated with the production of oil from the Kerogen. This occurs when the measure of Kerogen maturity (XVal) approaches
	XVal_Mean_Trans_1 value; where the standard deviation is XVal_Sig_Trans_1. The probability transistion 1 has occured is given as P_Trans_1 which is
	calculated from the Cummmulative Probability Distribution (CPD).
	The second transistion is associated with thermal cracking and the production of gas from the Kerogen. This occurs when the measure of Kerogen
	maturity (XVal) approaches XVal_Mean_Trans_2 value; where the standard deviation is XVal_Sig_Trans_2. The probability transistion 2 has occured is
	given as P_Trans_2 which is calculated from the Cummmulative Probability Distribution (CPD).
	The probability that the Kerogen is in a particular State (1, 2 or 3) can be calculated as:
	P_State_1 =(1 - P_Trans_1)*(1 - P_Trans_2)
	P_State_2 = P_Trans_1*(1 - P_Trans_2)
	P_State_3 =1 - P_State_1 - P_State_2
	In terms of the computed property there are two options, determined by the value of iOpt
	When iOpt=0 then each Kerogen state can have an associated property, where these properties are defined by YVal_State_1, YVal_State_2 and
	YVal_State_3. The corresponding value of the associated property (Y_Val) can therefore be determined as:
	Y_Val = YVal_State_1*P_State_1 + YVal_State_2*P_State_2 + YVal_State_3*P_State_3
	This option can be used when seeking to compute properties such as density and resistivity as a function of maturity.
	iOpt Controls the nature of the final property calculations:
	iOpt=0 Determine the average property value based on the arithmetic average of the individual state properties.
	iOpt=1 Determines the cummulative property value based on the sum of state values (this is typically used for computing comulative weight losses).
	
	Inputs:
	1. 	XVal:
	2.	YVal_State_1:
	3.	YVal_State_2:
	4.	YVal_State_3:
	5.	XVal_Mean_Trans_1:
	6.	XVal_Mean_Trans_2:
	7.	XVal_Sig_Trans_1:
	8.	XVal_Sig_Trans_2:
	9.	iOpt:
	Outputs:
	1.	FunVal:
	"""
#	1. Computations:
	Tiny=1E-20
	P_Trans_1 = fCPD(XVal,XVal_Mean_Trans_1, XVal_Sig_Trans_1) # Transition of kerogen from State #1 to State #2
	P_Trans_2 = fCPD(XVal,XVal_Mean_Trans_2, XVal_Sig_Trans_2) # Transition of kerogen from State #2 to State #3
	FunVal=0
	if(iOpt==0):
		P_State_1=(1-P_Trans_1)*(1-P_Trans_2)
		P_State_2=P_Trans_1*(1 - P_Trans_2)
		P_State_3=1-P_State_1-P_State_2
		FunVal=(YVal_State_1*P_State_1)+(YVal_State_2*P_State_2)+(YVal_State_3*P_State_3)
	if(iOpt==1):
		FunVal=YVal_State_1+P_Trans_1*YVal_State_2+P_Trans_2*YVal_State_3
	if(FunVal==0):
		FunVal=Tiny
	return FunVal
#
# A. ADDITIONAL FLUID COMPUTATION CODE FOR WATER:
# ===============================================
#
# A1. Temperature Corrected Water Resistivity:
#=============================================
def fRwTemperatureCorrected(Rw_Temp1, Temp1, Temp2):
	"""
	# This procedure takes the Rw value and one temperature Temp1, and computes
	# what the value should be at another temperature Temp2. All temperatures are in Deg C

	Inputs:
	1. Rw_Temp1 : Resistivity of Mud Filtrate at Temp 1 (ohm.m)
	2. Temp1 : Temperate of Mud Filtrate (degC)
	3. Temp2 : Temperature being applied (degC)

	Outputs:
	 - Rw_Temp2 - Resistivity of Mud Filtrate at Temp 2 (ohm.m)

	"""
	return Rw_Temp1 * ((Temp1 + 21.5) / (Temp2 + 21.5))
#
# A2. Water Salinity:
#====================
def fComputeSalinity(Rw, Temperature):
	"""
	Inputs:
	1. Rw : Water Resistivity (Ohmm)
	2. Temperature: Temperature (Deg C)

	Outputs:
	 - Salinity: Salinity (kppm)

	"""
	SLBChartTemperature=80
	Rw_ChartValue=fRwTemperatureCorrected(Rw,Temperature,SLBChartTemperature)
	x=log(Rw_ChartValue)/log(10)
	y = -0.0076*(x**5) + 0.0158*(x**4) + 0.0174*(x**3) - 0.015*(x**2) - 1.0706*x + 0.3561
	Salinity=10**y
	return Salinity
#
# A3. Water Density:
#====================
def fWaterDensity(Salinity, GasWaterRatio, Temperature, Pressure):
	"""
	This procedure calculates the density of water in g/cc Salinity is in kppm
	Temperature is in degrees Celsius and Pressure is in MPa but entered as Deg C. The calculation procedure
	is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.
	Note Brine density is considered to be broadly independent of Gas Water Ratio.

	Inputs:
	1. Salinity : Salinity (kppm)
	2. GasWaterRatio : Gas-Water Ratio (v/v)
	3. Temperature : Temperate (degC)
	4. Pressure : Pressure (psia)

	Outputs:
	 - RhoWater - Density of Water (g/cc)

	"""
	Temp = Temperature
	Press = Pressure / 145.038
	Sal = Salinity / 1000
	A = (-80 * Temp) + (-3.3 * (Temp**2)) + (0.00175 * (Temp**3))
	B = (489 * Press) + (-2 * Temp * Press) + (0.016 * (Temp**2) * Press)
	C = (-0.000013 * (Temp**3) * Press) + (-0.333 * (Press**2)) + (0.002 * Temp * (Press ** 2))
	PureWaterDensity = 1 + ((A + B + C) * 1e-6)
	A = 80 + (3 * Temp) + (-3300 * Sal) + (-13 * Press) + (47 * Press * Sal)
	B = (300 * Press) + (-2400 * Press * Sal)
	C = 0.000001 * (B + (Temp * A))
	D = 0.668 + (0.44 * Sal)
	return PureWaterDensity + (Sal * (D + C))
#
# A4. Water Hydrogen Index:
#==========================
def fWaterHydrogenIndex(Salinity, GasWaterRatio, Temperature, Pressure):
	"""
	The hydrogen index of a fluid is defined as the ratio of the number of hydrogen atoms per unit volume
	in the fluid, compared to pure water at STP (20 Deg C and 1 atmosphere).	
	Note: The procedure expects Salinity in kppm (i.e. g/Kg)

	Inputs:
	1. Salinity : Salinity (kppm)
	2. GasWaterRatio : Gas-Water Ratio (v/v)
	3. Temperature : Temperate (degC)
	4. Pressure : Pressure (psia)

	Outputs:
	 - HIWater - Hydrogen Index Water (unitless)

	"""	
	MWWater = 1.008 * 2 + 15.998 # Compute Molecular Weight of Water
	PureWaterDensity = fWaterDensity(0, 0, 20, 14.7)
	NHWater = PureWaterDensity * (2 / MWWater) # Estimated Number of Hydrogen Atoms per unit volume of pure water.
	BrineDensity = fWaterDensity(Salinity, GasWaterRatio, Temperature, Pressure)
	NHBrine = BrineDensity * (1 - (Salinity / 1000)) * (2 / MWWater)
	return NHBrine / NHWater # Compute Hydrogen Index
#
# A5. Water Acoustic Velocity:
#=============================
def fWaterAcousticVelocity(Salinity, GasWaterRatio, Temperature, Pressure):
	"""
	Caution: This procedure is under development and is only valid
	up to a pressure of 100 MPa.

	This procedure calculates the acoustic velocity of water in m/s from Salinity in kppm
	GasWaterRatio is constrained, Temperature in degrees Celsius, Pressure in Psia
	The calculation procedure is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.
	
	Wilson (1959) provides a relationship for the
	velocity VW of pure water to 100degC and about 100 MPa.

	Millero et al., (1977) and Chen et al., (1978) gave additional factors to be
	added to the velocity of water to calculate the effects of
	salinity. Their corrections, unfortunately, are limited to 55degC
	and 1 molal ionic strength (55 000 ppm). We can extend their
	results by using the data of Wyllie et al., (1956) to 100degC and
	150000 ppm NaCl.

	Inputs:
	1. Salinity : Salinity (kppm)
	2. GasWaterRatio : Gas-Water Ratio (v/v)
	3. Temperature : Temperate (degC)
	4. Pressure : Pressure (psia)

	Outputs:
	 - VP_water - Velocity of Water (m/s)

	"""	
	T = Temperature
	P = Pressure / 145.038
	S = Salinity / 1000 # Converts Salinity from kppm to ppm x1E-6
	a00 = 1402.85
	a10 = 4.871
	a20 = -0.04783
	a30 = 1.487e-4
	a40 = -2.197e-7
	a01 = 1.524
	a11 = -0.0111
	a21 = 2.747e-4
	a31 = -6.503e-7
	a41 = 7.987e-10
	a02 = 3.437e-3
	a12 = 1.739e-4
	a22 = -2.135e-6
	a32 = -1.455e-8
	a42 = 5.230e-11
	a03 = -1.197e-5
	a13 = -1.628e-6
	a23 = 1.237e-8
	a33 = 1.327e-10
	a43 = -4.614e-13
	W =  [[a00,a01,a02,a03]]
	W += [[a10,a11,a12,a13]]
	W += [[a20,a21,a22,a23]]
	W += [[a30,a31,a32,a33]]
	W += [[a40,a41,a42,a43]]

	# Wilson (1959) provides a relationship for the
	# velocity VW of pure water to 100degC and about 100 MPa.
	VP_water = 0
	for i in range(0, 5):
		for j in range(0, 4):
			VP_water += W[i][j] * (T**i) * (P**j)

	# Millero et al., (1977) and Chen et al., (1978) gave additional factors to be
	# added to the velocity of water to calculate the effects of
	# salinity. Their corrections, unfortunately, are limited to 55degC
	# and 1 molal ionic strength (55 000 ppm). We can extend their
	# results by using the data of Wyllie et al., (1956) to 100degC and
	# 150000 ppm NaCl.
	#
	A = 1170 - (9.6*T) + (0.055*(T**2)) - (8.5e-5*(T**2)) + (2.6*P) - (0.0029*T*P) - (0.0476*(P**2))
	B = 780 - (10*P) + (0.16*(P**2))
	C = (A*S) + (B*(S**1.5)) - (1820*(S**2))
	VP_brine = VP_water + C
	
	Rho_brine = fWaterDensity(Salinity, GasWaterRatio, Temperature, Pressure) * 1000 # Kg/m3
	K_Brine = Rho_brine * (VP_brine**2)
	# GWRMax = fMaxGasWaterRatio(Salinity, Temperature, Pressure) # NOT USED
	GWRMax=0.000
	GasWaterRatio = ImposeLimits(GasWaterRatio, 0, GWRMax)
	KGasBrine = K_Brine / (1 + (0.0494*GasWaterRatio))
	return (KGasBrine / Rho_brine) ** 0.5
#
# A6. Maximum Gas Water Ratio:
#=============================
def fMaxGasWaterRatio(Salinity, Temperature, Pressure):
	"""
	This function returns the maximum gas water ratio value.
	The calculation procedure is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.

	Inputs:
	1. Salinity : Salinity (kppm)
	2. Temperature : Temperate (degC)
	3. Pressure : Pressure (psia)

	Outputs:
	 - GWR_max - Maximum Gas Water Ratio (v/v)

	"""
	Temp = Temperature # Deg C
	Press = Pressure / 145.038 # MPa
	Sal = Salinity
	A = log(0.712 * Press * ((abs(Temp - 76.71)) ** 1.5) + 3676 * (Press ** 0.64)) / log(10)
	B = -4 - 7.786 * Sal * (Temp + 17.78) ** -0.306
	C = A + B
	return 10**C
#
# B. ADDITIONAL FLUID COMPUTATION CODE FOR HYDROCARBONS:
# ======================================================
# B.1 Gas Density:
#=================
def fGasDensity(GasGravity, Temperature, Pressure):
	"""
	This procedure computes gas density (g/cc).
	Temperature in entered in Deg C but calculations are in Deg K
	Pressure in entered in psia but calculations are in MPa
	Note: Natural gas is characterised by its gravity (i.e. GasGravity), for methane
	this value is 0.56, however, it may be as high as 1.8 for heavier natural gases.
	The calculation procedure is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.

	Inputs:
	1. GasGravity : Gas Gravity (g/cc)
	2. Temperature : Temperate (degC)
	3. Pressure : Pressure (psia)

	Outputs:
	 - GasDensity - Gas Density (g/cc)

	"""
	GasConstant = 8.314
	Press = Pressure / 145.038 # MPa
	Temp = Temperature + 273.16 # Deg K
	Pr = Press / (4.892 - (0.4048 * GasGravity))
	Tr = Temp / (94.72 + (170.75 * GasGravity))
	A = 0.03 + 0.00527 * ((3.5 - Tr)**3)
	B = (0.642 * Tr) - (0.007 * (Tr**4)) - 0.52
	C = 0.109 * ((3.85 - Tr)**2)
	D = exp(-((0.45 + (8 * ((0.56 - (1 / Tr))**2))) * ((Pr**1.2) / Tr)))
	Z = (A * Pr) + B + (C * D)
	return (28.8 * GasGravity * Press) / (Z * GasConstant * Temp)
#
# B.2 Gas Hydrogen Index:
#========================
def fGasHydrogenIndex(GasGravity, Temperature, Pressure):
	"""
	The hydrogen index of a fluid is defined as the ratio of the number of hydrogen atoms per unit volume
	in the fluid, compared to pure water at STP (20 Deg C and 1 atmosphere).

	Inputs:
	1. GasGravity : Gas Gravity (g/cc)
	2. Temperature : Temperate (degC)
	3. Pressure : Pressure (psia)

	Outputs:
	 - GasHydrogenIndex - Gas Hydrogen Index (unitless)

	"""
	GasDensity = fGasDensity(GasGravity, Temperature, Pressure)
	PureWaterDensity = fWaterDensity(0, 0, 20, 14.7)
	MWWater = 1.008 * 2 + 15.998
	MWAir = 28.96443 # By definition.
	MWGas = MWAir * GasGravity  # Gas Gravity is defined as MWGas/MWAir - values typically range from 0.55 to 1.50
	NHGasMolecule = 0.1427 * MWGas + 1.7123 # Based on a plot of Number of Hydrogen Atoms per molecule vs Molecular Weight of Alkanes.
	if NHGasMolecule < 4:
	 	NHGasMolecule = 4
	NHWater = PureWaterDensity * (2 / MWWater)
	NHGas = GasDensity * NHGasMolecule / MWGas
	return NHGas / NHWater
#
# B.3 Maximum Gas Oil Ratio (Scf/bbl):
#=====================================
def fMaxGasOilRatio(APIGravity, GasGravity, Temperature, Pressure):
	"""
	This procedure computes the maximum gas oil ratio (l/l) from APIGravity,
	Temperature (Deg C) and Pressure (Psia)

	Inputs:
	1. APIGravity : API Gravity (deg)
	2. GasGravity : Gas Gravity (g/cc)
	3. Temperature : Temperate (degC)
	4. Pressure : Pressure (psia)

	Outputs:
	 - GOR_max - Gas-Oil Ratio Maximum (ratio)

	"""
	T = Temperature
	P = Pressure / 145.0378 # Converts Pressure from Psia to MPa
	Rho_0 = (141.5 / (APIGravity + 131.5))
	A = P * (exp((4.072 / Rho_0) - (0.00377 * T)))
	return (0.02123 * GasGravity) * (A**1.205)*(158.9873/28.3168) # converts l/l to scf/bbl
#
# B.4 Oil Density:
#=================
def fOilDensity(APIGravity, GasOilRatioOFU, GasGravity, Temperature, Pressure):
	"""
	This procedure computes oil density (g/cc) from APIGravity
	GasGravity, GasOilRatio (l/l), Temperature (Deg C) and Pressure (MPa) but entered in psia
	The calculation procedure is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.

	Inputs:
	1. APIGravity : API Gravity (deg)
	2. GasOilRatioOFU : Gas-Oil Ratio (scf/bbl)
	3. GasGravity : Gas Gravity (g/cc)
	4. Temperature : Temperate (degC)
	5. Pressure : Pressure (psia)

	Outputs:
	 - RhoOil - Oil Density (g/cc) at Pressure and Temperature

	"""	
	T = Temperature
	P = Pressure / 145.038 # converts psia to MPa.
	GasOilRatio=GasOilRatioOFU*(28.3168/158.9873) # Converts scf/bbl to l/l

	# A reference density that can be used to characterize an oil Rho_0 is measured
	# at 15.6 degC and atmospheric pressure.
	Rho_0 = 141.5 / (APIGravity + 131.5)

	# B_0 is a volume factor derived by Standing (1962)
	B_0 = 0.972 + 0.00038 * ((2.4 * GasOilRatio * ((GasGravity/Rho_0)**0.5) + T + 1.78)**1.175)

	# True densities of live oils are also calculated using B_0, but
	# the mass of dissolved gas must be included.
	Rho_G = (Rho_0 + 0.0012*GasGravity*GasOilRatio) / B_0

	# The pressure dependence is comparatively small and the published data for density at
	# pressure pp can be described by the polynomial
	Rho_GP = Rho_G + (0.00277*P - 1.71e-7*(P**3)) * ((Rho_G - 1.15)**2) + (3.49e-4*P)

	# The effect of temperature is larger, and one of the most
	# common expressions used to calculate the in-situ density
	# was developed by Dodson and Standing (1945).
	# Rho_T = Rho_P / (0.972 + 0.000381 * ((T + 17.78) ** 1.175))
	# This is accounted for in the B_0 and Rho_G terms which collapse when GasOilRation = 0

	return Rho_GP
#
# B.5 Oil Hydrogen Index:
#========================
def fOilHydrogenIndex(OilDensity):
	"""
	Reference:  Gaymard, R, and Poupon, A., "Response of Neutron and Formation
	Density Logs in Hydrocarbon Bearing Formations,"  The Log Analyst 9(5), 3-12(1968).

	HI_oil = (9 * Rho_oil) * (0.15 + 0.2 * (0.9 - Rho_oil)**2)

	# EDIT
	Taken as a 5th-degree polynomial fit from Schlumberger's Log Interpretation
	Chart Book p.16

	Inputs:
	1. OilDensity : Oil Density (g/cc)

	Outputs:
	 - HIOil - Hydrogen Index Oil (unitless)

	"""
	return sum([e*(OilDensity**i) for i, e in enumerate([0.0284, 1.7878, 1.0669, -4.0961, 3.1585, -0.9487])])
#
# B.6 Gas Bulk Modulus:
#======================
def fGasBulkModulus(GasGravity, Temperature, Pressure):
	"""
	This procedure computes gas Adiabatic Bulk Modulus (Pa)
	Note: Natural gas is characterised by its gravity (i.e. GasGravity), for methane
	this value is 0.56, however, it may be as high as 1.8 for heavier natural gases.
	The calculation procedure is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.
	Pressure is entered in psia.
	Temperature is entered in Deg C
	Answer in Pascals only
	Note all function calculations are made in SI units: for converstions are necessary:
	Inputs:
	1. GasGravity : Gas Gravity (g/cc)
	2. Temperature : Temperate (degC)
	3. Pressure : Pressure (psia)
	Outputs:
	1. KDYN_adiabatic - Adiabatic Bulk Modulus (Pa)
	"""
	GasConstant = 8.314
	Temp = Temperature + 273.16 # Deg K
	Press = (Pressure / 145.038) # MPa
	Pr = Press / (4.892 - (0.4048 * GasGravity))
	Tr = Temp / (94.72 + (170.75 * GasGravity))
	A = 0.03 + (0.00527 * ((3.5 - Tr)**3))
	B = (0.642 * Tr) - (0.007 * (Tr**4)) - 0.52
	C = 0.109 * ((3.85 - Tr)**2)
	D = exp(-((0.45 + (8 * ((0.56 - (1 / Tr))**2))) * ((Pr ** 1.2) / Tr)))
	Z = (A * Pr) + B + (C * D)
	Rg = ((28.8 * GasGravity * Press) / (Z * GasConstant * Temp))
	G = 0.85 + (5.6 / (Pr + 2)) + (27.1 / ((Pr + 3.5)**2)) - (8.7 * exp(-0.65 * (Pr + 1)))
	M = (1.2 * (-1 * (0.45 + (8 * ((0.56 - (1 / Tr))**2))) * ((Pr**0.2) / Tr)))
	F = (C * D * M) + A
	return 1e6 * (((Press * G) / (1-(Pr * F / Z)))) # Pa
#
# B.7 Gas Acoustic Velocity:
#===========================
def fGasAcousticVelocity(GasGravity, Temperature, Pressure):
	"""
	This procedure computes gas acoustic velocity (m/s).
	Note: Natural gas is characterised by its gravity (i.e. GasGravity), for methane
	this value is 0.56, however, it may be as high as 1.8 for heavier natural gases.
	The calculation procedure is taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.
	Inputs:
	1. GasGravity : Gas Gravity (g/cc)
	2. Temperature : Temperate (degC)
	3. Pressure : Pressure (psia)
	Outputs:
	1. VP_gas - Gas Acoustic Velocity (m/s)
	"""
	GasBulkModulus = fGasBulkModulus(GasGravity, Temperature, Pressure) # Pascals
	GasDensity = fGasDensity(GasGravity, Temperature, Pressure) * 1000 # Kg
	return (GasBulkModulus / GasDensity)**0.5  # m/s
#
# B.8 Oil Density:
#=================
def fOilAcousticVelocity(APIGravity, GasOilRatioOFU, GasGravity, Temperature, Pressure):
	"""
	This procedure computes oil acoustic velocity (m/s) from APIGravity
	GasGravity, GasOilRatio (m3/m3), Temperature (Deg C) and Pressure (MPa)
	The calculation procedure is based taken from Batzle and Wang. Geophys., 57, 1396 - 1408. 1992.
	Inputs:
	1. APIGravity : API Gravity (deg)
	2. GasOilRatioOFU : Gas-Oil Ratio (ratio)
	3. GasGravity : Gas Gravity (g/cc)
	4. Temperature : Temperate (degC)
	5. Pressure : Pressure (psia)
	Outputs:
	 - VP_oil - Oil Velocity (m/s)
	"""	
	T = Temperature
	P = Pressure / 145.0378 # Converts Pressure from Psia to MPa
	GasOilRatio=GasOilRatioOFU*(28.3168/158.9873)  # Converts scf/bbl to l/l
	# A reference density that can be used to characterize an oil Rho_0 is measured
	# at 15.6 degC and atmospheric pressure.
	Rho_0 = 141.5 / (APIGravity + 131.5)
	# B_0 is a volume factor derived by Standing (1962)
	B_0 = 0.972 + 0.00038 * ((2.4 * GasOilRatio * ((GasGravity/Rho_0)**0.5) + T + 1.78)**1.175)
	# Seismic properties of a live oil are estimated by considering
	# it to be a mixture of the original gas-free oil and a light
	# liquid representing the gas component. Velocities can still be
	# calculated by substituting a pseudodensity Rho_Prime based on the
	# expansion caused by gas intake.
	# Collapses to  Rho_Prime = (Rho_0/B_0) when GOR = 0
	Rho_Prime = (Rho_0/B_0) * ((1 + 0.001*GasOilRatio)**-1)
	# Compute Oil Acousic Velocity.
	A = (2096 * ((Rho_Prime / (2.6 - Rho_Prime))**0.5)) - (3.7*T) + (4.64*P)
	B = 0.0115 * ((4.12 * (((1.08 * (Rho_Prime**-1)) - 1)**0.5)) - 1) * T*P
	return A + B
#
# C. GENERAL MATHS FUNCTIONS:
#============================
#
# C.1 Imposing Limits:
#=====================
def ImposeLimits(Val, MinVal, MaxVal):
	"""
	Equivalent to min(max(Val, MinVal), MaxVal)
	Inputs:
	1. Val : Value to limit (any)
	2. MinVal : Value Minimum Limit (any)
	3. MaxVal : Value Maximum Limit (any)
	Outputs:
	 - LimitedVal : Limited Value (any)
	"""
	if MinVal < Val < MaxVal:
		return Val
	elif Val <= MinVal:
		return MinVal
	elif Val >= MaxVal:
		return MaxVal
#
# C.2 Interpolation:
#===================
def fInterpol(X1, X2, Y1, Y2, X):
	return (Y2 - Y1) * (X - X1) / (X2 - X1) + Y1
#
# C.3 Matrix Inversion:
#=====================
def gauss_jordan(m, eps=1.0/(10**10)):
	"""
	return True or False for Gauss - gauss_jordan
	Inputs:
	1. m : Matrix (list of lists)
	2. eps [=1.0/(10**10)] : epsilon, a tiny error (~0.001)
	Outputs:
	 - GJ : Gauss Jordan (Bool)
	"""
	(h, w) = (len(m), len(m[0]))
	for y in range(0,h):
		maxrow = y
		for y2 in range(y+1, h):    # Find max pivot
			if abs(m[y2][y]) > abs(m[maxrow][y]):
				maxrow = y2
		(m[y], m[maxrow]) = (m[maxrow], m[y])
		if abs(m[y][y]) <= eps:     # Singular?
			return False
		for y2 in range(y+1, h):    # Eliminate column y
			c = m[y2][y] / m[y][y]
			for x in range(y, w):
				m[y2][x] -= m[y][x] * c
	for y in range(h-1, 0-1, -1): # Backsubstitute
		c  = m[y][y]
		for y2 in range(0,y):
			for x in range(w-1, y-1, -1):
				m[y2][x] -=  m[y][x] * m[y2][y] / c
		m[y][y] /= c
		for x in range(h, w):       # Normalize row y
			m[y][x] /= c
	return True
#
def SolveAndCorrect(M, b):
	"""
	Call Solve and MatrixCorrections in order.
	"""
	XMatrix = Solve(M, b)
	XMatrix, Qc = MatrixCorrections(XMatrix)
	return XMatrix, Qc
#
def Solve(M, b):
	"""
	Solves M*x = b
	return vector x so that M*x = b
	Inputs:
	1. M : Matrix (list of lists)
	2. b : Vector (list of scalars)
	Outputs:
	 - x : Matrix; solution to M*x = b (list of lists)
	"""
	m2 = [row[:]+[right] for row,right in zip(M,b) ]
	return [row[-1] for row in m2] if gauss_jordan(m2) else None
#
def inv(M):
	"""
	return the inv of the matrix M
	Inputs:
	1. M : Matrix (list of lists)
	Outputs:
	 - invM : Inverse of M (M^-1) (list of lists)
	"""
	#clone the matrix and append the identity matrix
	# [int(i==j) for j in range_M] is nothing but the i(th row of the identity matrix
	m2 = [row[:]+[int(i==j) for j in range(len(M) )] for i,row in enumerate(M) ]
	# extract the appended matrix (kind of m2[m:,...]
	return [row[len(M[0]):] for row in m2] if gauss_jordan(m2) else None
#
def zeros(s, zero=0):
	"""
	return a matrix of size `s`
	Inputs:
	1. s : size - a tuple containing dimensions of the matrix (tuple)
	2. zero [=0] : the value to use to fill the matrix (number)
	"""
	return [zeros(s[1:] ) for i in range(s[0] ) ] if not len(s) else zero
#
def MatrixCorrections(x):
	"""
	Inputs:
	1. x : Matrix (list of lists)
	Outputs:
	 - x : Corrected Matrix (list of lists)
	 - QC : QC for corrections where volume vector has a (non-physical) negative element
	"""
	h = len(x)
	QC = 0
	for i in range(0, h):
		QC = QC + abs(x[i])
	QC = abs(1 - QC)
	for i in range(0, h):
		if x[i] < 0:
			x[i] = 0.000
	summ = 0.000
	for i in range(0, h):
		summ = summ + x[i]
	for i in range(0, h):
		if summ > 0:
			x[i] = x[i] / summ
		else:
			print x
			print summ
	summ = 0
	for i in range(0, h):
		summ = summ + x[i]
	if summ > 0:
		x[i] = x[i] / summ
	else:
		print x
		print summ
	if(abs(summ-1)>=0.000001):
		print "Inversion Error",summ,h,x
	return x, QC
#
def ComputeMatrixDifference(A,B):
	"""
	Function computes the Root Mean Squared (RMS) Error for the difference
	between two matrix.
	Inputs:
	1.  Matrix A
	2.  Matrix B
	Outputs:
	1. 	Delta: Error due to differences in matrix element values
	"""
	na=len(A)
	nb=len(B)
	Delta=0
	if(na==nb):
		for i in range(0,na):
			Delta=Delta+abs(A[i]-B[i])**2
#			print i,A[i],B[i],Delta
		Delta=(Delta/na)**0.5
	else:
		Delta=1
	return Delta
#
def fCPD(X_Val,X_Mean,X_Sig):
	"""
	Function F_CDF calculates the cummulative probability distribution for a normally distributed property:
	Inputs:
	1. X_Val: Corresponds to the value of x in the cummulative probability distribution (CPD)
	2. X_Mean: corrresponds to the mean value of x in the cummulative probability distribution (CPD)
	3. X_Sig: corresponds to the standard deviation of x in the cummulative probability distribution (CPD)
	Outputs:
	1. FunValue: returns a CDF value between 0 and 1.
	"""
#   1. Initialisation:
	NVal=-1
	NMax=67
	FunValue=0
	FunTerm=0
	iSign=1
	iEnd=0 # False
	Pi=3.141592653589793
#	2. Error Trapping:
	if(X_Sig==0):
		X_Sig=1
#	3. Computations:
	x=((X_Val-X_Mean)/(X_Sig*(2**0.5)))
	while iEnd==0: # False
		NVal=NVal+1
		if(NVal<=NMax):
			iEnd=0 # False
			FunTerm = iSign*(x**(2*NVal+1))/(fFactorial(NVal)*(2*NVal+1))
			if(iSign==1):
				iSign=-1
			else:
				iSign=1
		else:
			iEnd=1 # True
			FunTerm=0
		FunValue=FunValue+FunTerm
	FunValue=(2/(Pi**0.5))*FunValue # FunValue Corresponds to Erf(x)
	FunValue=(1/ 2)*(1+FunValue) # FunValue Corresponds to CPD(x)
	FunValue=ImposeLimits(FunValue,0,1)
	return FunValue
#
def fFactorial(N):
	"""
	Function calculates the factorial of N (i.e. N!, where N is an integer):
	Inputs:
	1. N: Corresponds to the integer N
	Outputs:
	1. Total: Returns the value of N!
	"""
#	1. Initialisations:
	iNVal = int(N)
	Total=1
	LargeNumber = 1E+99
	iEnd=0
#	2.	Computations:
	I=0
	if(iNVal>=1):
		while iEnd==0:
			if(iNVal<=66):
				I=I+1
				if(I==1):
					Total=I
				else:
					Total=Total*I
				if(I==iNVal):
					iEnd=1
			else:
				iEnd=1
				Total=LargeNumber
	else:
		Total=1
	return Total
#
# D. RESPONSE EQUATIONS:
#=======================
#
# D1. Linear Response Function:
#==============================
def fLinear(Vc1,Vc2,Vc3,Vk,Vw,Va,Vf,Pc1,Pc2,Pc3,Pk,Pw,Pa,Pf):
	"""
	Function generates a linear response function
	Inputs:
	1.	Vc1		-	Volume of component #1
	2.	Vc2		-	Volume of component #2
	3.	Vc3		- 	Volume of component #3
	4.	Vk		-	Volume of kerogen 
	5.	Vw		-	Volume of water in effective (i.e. non-microporous) pore space
	6.	Va		-	Volume of adsorbed hydrocarbon component in effective (i.e. non-microporous) pore space
	7. 	Vf		-	Volume of free hydrocarbon component in effective (i.e. non-microporous) pore space
	8. 	Pc1		- 	Property of component #1
	9.	Pc2		-	Property of component #2
	10.	Pc3		-	Property of component #3
	11. Pk		-	Property of kerogen 
	12. Pw		-	Property of water
	13. Pa		- 	Property of adsorbed hydrocarbon component
	14. Pf		-	Property of free hydrocarbon hydrocarbon component
	Output:
	1.	Lrf		- 	Linear response function
	
	"""
#
#   1. Normalise volumetric components:
#	-----------------------------------
	Sum=abs(Vc1)+abs(Vc2)+abs(Vc3)+abs(Vk)+abs(Vw)+abs(Va)+abs(Vf)
	Vc1=abs(Vc1)/Sum
	Vc2=abs(Vc2)/Sum
	Vc3=abs(Vc3)/Sum
	Vk=abs(Vk)/Sum
	Vw=abs(Vw)/Sum
	Va=abs(Va)/Sum
	Vf=abs(Vf)/Sum
#
#	2. Compute liear response function:
#	-----------------------------------
	Lrf=Vc1*Pc1+Vc2*Pc2+Vc3*Pc3+Vk*Pk+Vw*Pw+Va*Pa+Vf*Pf
#
#   3. Output result:
#	-----------------
	return Lrf
#
# D2. CRIM Resistivity Model Function:
#=====================================
def fRCrim(Swe,Vc1,Vc2,Vc3,Vk,PHIe,Rc1,Rc2,Rc3,Rk,Rw,Rh,Cwv,Ckv,Alpha,Tout):
	"""
	Function generates a resistivity response function based on the CRIM 
	Inputs:
	1.	Swe		-	Effective Water Saturation (frac)
	2.	Vc1		-	Volume of component #1
	3.	Vc2		-	Volume of component #2
	4.	Vc3		- 	Volume of component #3
	5.	Vk		-	Volume of kerogen 
	6.	PHIe	-	Effective Porosity
	7.	Rc1		- 	Resistivity of component #1
	8.	Rc2		-	Resistivity of component #2
	9.	Rc3		-	Resistivity of component #3
	10. Rk		-	Resistivity of kerogen 
	11. Rw		-	Resistivity of water
	12. Rh		-	Resistivity of hydrocarbon component - Note: It is assumed that the resistivity of the adsorbed and free gas are the same (Ra=Rf).
	13.	Cwv		-	Critical Water Volume 
	14.	Ckv		-	Critical Kerogen Volume
	15.	Alpha	-	CRIM Mixing Law Exponent
	16. Tout    -   Output type (0=Conductivity,1=Resistivity)
	Output:
	1.	Fr		- 	Function response
	"""
#
#   1. Compute and normalise volumetric components:
#	-----------------------------------------------
	Vw=PHIe*Swe
	Vh=PHIe*(1-Swe)
	Vwe=(Vw-Cwv)/(1-Cwv)
	Vwe=ImposeLimits(Vwe,0,1)
	Vke=(Vk-Ckv)/(1-Ckv)
	Vke=ImposeLimits(Vke,0,1)
	Sum=abs(Vc1)+abs(Vc2)+abs(Vc3)+abs(Vke)+abs(Vwe)+abs(Vh)
	Vc1=abs(Vc1)/Sum
	Vc2=abs(Vc2)/Sum
	Vc3=abs(Vc3)/Sum
	Vk=abs(Vk)/Sum
	Vw=abs(Vw)/Sum
	Vh=abs(Vh)/Sum
#
#	2. Determine conductivity of components:
#	----------------------------------------
	Sigc1=1/Rc1
	Sigc2=1/Rc2
	Sigc3=1/Rc3
	Sigk=1/Rk
	Sigw=1/Rw
	Sigh=1/Rh
#
#	3. Compute Conductivity:
#	========================
	Trm1=Vc1*(Sigc1**(1/Alpha))
	Trm2=Vc2*(Sigc2**(1/Alpha))
	Trm3=Vc3*(Sigc3**(1/Alpha))
	Trm4=(Vk**2.2)*(Sigk**(1/Alpha)) # Factor of 2.2 included to get data to fit to Yang et al
	Trm5=Vw*(Sigw**(1/Alpha))
	Trm6=Vh*(Sigh**(1/Alpha))
	Crf=(Trm1+Trm2+Trm3+Trm4+Trm5+Trm6)**Alpha
#
#
#   4. Output result:
#	-----------------
	if(Tout==0):
		Fr=Crf
	else:
		Fr=1/Crf
	return Fr
#
# D3. TOC-Wt Fraction CALCULATIONS:
#==================================
def fToc_Wtf(Vc1,Vc2,Vc3,Vk,Vrw,Ck,Dc1,Dc2,Dc3,Dk,Dw):
	"""
	Function calculates Total Organic Carbon (weight fraction).
	Inputs:
	1.	Vc1		-	Volume of component #1
	2.	Vc2		-	Volume of component #2
	3.	Vc3		- 	Volume of component #3
	4.	Vk		-	Volume of kerogen 
	5.	Vrw		-	Volume of residual water in the effective pore space under laboratory conditions
	6.	Ck		-	Weight of carbon per unit weight of organic matter
	7.	Dc1		- 	Density of component #1
	8.	Dc2		-	Density of component #2
	9.	Dc3		-	Density of component #3
	10. Dk		-	Resistivity of kerogen 
	11. Dw		-	Resistivity of water
	Output:
	1.	Tocwf	- 	Total organic carbon weight fraction
	"""
	GDen=fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw)
	Tocwf=Vk*Ck*Dk/GDen
	return Tocwf
#
# D4. ORGANIC RICH MUDSTONE GRAIN DENSITY CALCULATIONS:
#======================================================
def	fOrmGDen(Vc1,Vc2,Vc3,Vk,Vrw,Dc1,Dc2,Dc3,Dk,Dw):
	"""
	Function calculates grain density for an organic rich mudstone
	Inputs:
	1.	Vc1		-	Volume of component #1
	2.	Vc2		-	Volume of component #2
	3.	Vc3		- 	Volume of component #3
	4.	Vk		-	Volume of kerogen 
	5.	Vrw		-	Volume of residual water in the effective pore space under laboratory conditions
	6.	Dc1		- 	Density of component #1
	7.	Dc2		-	Density of component #2
	8.	Dc3		-	Density of component #3
	9. 	Dk		-	Resistivity of kerogen 
	10. Dw		-	Resistivity of water
	Output:
	1.OrmGDen	- 	Total organic carbon weight fraction
	"""
	Sum=Vc1+Vc2+Vc3+Vk+Vrw
	OrmGDen=(Vc1*Dc1+Vc2*Dc2+Vc3*Dc3+Vk*Dk+Vrw*Dw)/Sum
	return OrmGDen
#
def MaxRecoveryORM(Vc1,Vc2,Vc3,Vk,Vw,Va,Vf,Dc1,Dc2,Dc3,Dk,Dw,Da,Df,Adsorrption_Model,RSK_In,PK,PI,PF,FOut):
	"""
	This function calculates the total in place hydrocarbon volume and the maximum recoverable volume of gas based on
	the difference between the initial formation pressure and the final abandonment pressure. The specific units are defined
	by the FOut flag.
	Inputs:
	1.	Vc1		-	Volume of component #1
	2.	Vc2		-	Volume of component #2
	3.	Vc3		- 	Volume of component #3
	4.	Vk		-	Volume of kerogen 	#4
	5.	PHIe	-	Effective Porosity #5 = Vw+Va+Vf
	6.	Swe		-	Effective Water Saturation #6 = Vw/(Vw+Va+Vf)
	8.	Dc1		-	Density of component #1
	9.	Dc2		-	Density of component #2
	10.	Dc3		- 	Density of component #3
	11.	Dk		-	Density of kerogen 	#4
	12.	Dw		- 	Density of water  	#5
	13.	Da		-	Density of adsorbed gas #6
	14.	Df		-	Density of free gas #7
	15.	Adsorrption_Model	-	Defines adsorption model used.
	16,	RSK_In		Ratio of volume of adsorbed gas to kerogen
	17.	PK			Pressure constant used in Langmuir model.
	18.	PI			Initial Pressure (Psia)
	19.	PF			Final Pressure (Psia)
	20.	TOut		Output results in cm3/g at STP (TOut=0) or SCF/Ton (TOut=1)
	Outputs:
	1.	IFD			Initial formation density (g/cm3)
	2.	IPV			In Place Volume (cm3/g) - Based on mass of formation.
	3.	MRV			Maximum Recoverable Volume (cm3/g)
	4.	RF			Recovery Factor (frac)
	"""
#
#	1. Define conversion factors and Standard Temperature and Pressure (STP) conditions:
#	====================================================================================
	TSTD=20.00	# Standard Temperature is 20 Deg C
	PSTD=14.7	# Standard Pressure is 14.7 psi or 1 atm

#	2. Compute volumes of water and hydrocarbon components:
#	=======================================================
	Vw=PHIe*Swe # Volume of water
	Vh=PHIe*(1-Swe) # Volume of hydrocarbons
#
#	3. Define volumes of free and adsorbed gas at reservoir conditions:
#	===================================================================
	if(Adsorrption_Model=="1. Fixed RSK Value"):
		Va=RSK_In*Vk
	else:
		Va=RSK_In*Vk*(PI/PF)/(1+(PI/PK))
	if(Va>=Vh):
		Va=Vh
	Vf=Vh-Va
#
#	4. Calculate the density of the formation at reservoir conditions:
#	===============================================================
	IFD=Vc1*Dc1+Vc2*Dc2+Vc3*Dc3+Vk*Dk+Vw*Dw+Va*Da+Vf*Df
#
#	5. Calculate the volume of gas per gram of rock at reservoir conditions in cm3:
#	===============================================================================
	IPV=(Va+Vf)/IFD
	

def GIPsurfORM(GDEN, HADS, HFRE, PHIT, SWT, Dw, Dg, Da, STPw, STPg):
	
	
#	1. Define conversion factors and Standard Temperature and Pressure (STP) conditions:
#	====================================================================================
	TSTD=0.00	# Standard Temperature is 0 Deg C
	PSTD=14.696	# Standard Pressure is 14.7 psi or 1 atm
	SIMP=32.05066882 # cc/g to scf/ton (short tons)

#	2. Calculate intermediate values and masses of formation at reservoir conditions:
#	====================================================================================
	vMAT=1.0-PHIT # matrix volume including kerogen
	vW=SWT*PHIT # water volume
	mMAT=vMAT*GDEN # mass of 1cm3 of formation
	mADS=HADS*Da # mass of 1 unit of adsorbed gas per formation unit
	mFRE=HFRE*Dg # mass of 1 unit of free gas per formation unit
	
#	2. Calculate intermediate values and masses of formation at STP conditions:
#	====================================================================================	
	vMATstp = vMAT # rocks don't expand too much (we hope!)
	vADSstp = mADS/STPg # convert volume HADS to STP gas, assume full desorption
	vFREstp = mFRE/STPg # convert volume HFRE to STP gas, assume no loss
	GIP = vADSstp + vFREstp # total GIP in cc/g
	return vADSstp, vFREstp, GIP

__doc__ = """ORMPIMS_CODE

Saved 20th February 2019

Modified by KB 25/06/2020:
- added function for STP volume conversions"""
__author__ = """Tim PRITCHARD (tnp1)"""
__date__ = """2018-02-22"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""