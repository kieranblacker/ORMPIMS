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
#Type:Variable
#BName:Depth
#Family:Measured Depth
#Unit:ft
#Mode:In
#Description:Measured Depth
MD = Variable("Becconsall-1Z", "LQC", "MD", u"Measured Depth", u"ft")
parameterDict.update({'MD' : Parameter(name='MD',bname='Depth',type='Variable',family='Measured Depth',measurement='',unit='ft',value='Becconsall-1Z.LQC.MD',mode='In',description='Measured Depth',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:Tvd
#Family:True Vertical Depth
#Unit:ft
#Mode:In
#Description:True Vertical Depth
TVD = Variable("Becconsall-1Z", "LQC", "TVD", u"True Vertical Depth", u"ft")
parameterDict.update({'TVD' : Parameter(name='TVD',bname='Tvd',type='Variable Optional',family='True Vertical Depth',measurement='',unit='ft',value='Becconsall-1Z.LQC.TVD',mode='In',description='True Vertical Depth',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:Cali
#Family:Caliper
#Unit:in
#Mode:In
#Description:Caliper
CALI = Variable("Becconsall-1Z", "LQC", "CALI", u"Caliper", u"in")
parameterDict.update({'CALI' : Parameter(name='CALI',bname='Cali',type='Variable Optional',family='Caliper',measurement='',unit='in',value='Becconsall-1Z.LQC.CALI',mode='In',description='Caliper',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Gr
#Family:Gamma Ray
#Unit:gAPI
#Mode:In
#Description:Gamma Ray
GR = Variable("Becconsall-1Z", "LQC", "GR", u"Gamma Ray", u"gAPI")
parameterDict.update({'GR' : Parameter(name='GR',bname='Gr',type='Variable',family='Gamma Ray',measurement='',unit='gAPI',value='Becconsall-1Z.LQC.GR',mode='In',description='Gamma Ray',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:Rhob
#Family:Bulk Density
#Unit:g/cm3
#Mode:In
#Description:Density
RHOB = Variable("Becconsall-1Z", "LQC", "RHOB", u"Bulk Density", u"g/cm3")
parameterDict.update({'RHOB' : Parameter(name='RHOB',bname='Rhob',type='Variable Optional',family='Bulk Density',measurement='',unit='g/cm3',value='Becconsall-1Z.LQC.RHOB',mode='In',description='Density',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:Drho
#Family:Bulk Density Correction
#Unit:g/cm3
#Mode:In
#Description:Density Correction
DRHO = Variable("Becconsall-1Z", "LQC", "DRHO", u"Bulk Density Correction", u"g/cm3")
parameterDict.update({'DRHO' : Parameter(name='DRHO',bname='Drho',type='Variable Optional',family='Bulk Density Correction',measurement='',unit='g/cm3',value='Becconsall-1Z.LQC.DRHO',mode='In',description='Density Correction',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:Phin
#Family:Neutron Porosity
#Unit:frac
#Mode:In
#Description:Neutron Porosity
PHIN = Variable("Becconsall-1Z", "LQC", "PHIN", u"Neutron Porosity", u"frac")
parameterDict.update({'PHIN' : Parameter(name='PHIN',bname='Phin',type='Variable Optional',family='Neutron Porosity',measurement='',unit='frac',value='Becconsall-1Z.LQC.PHIN',mode='In',description='Neutron Porosity',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:Dtco
#Family:Compressional Slowness
#Unit:us/ft
#Mode:In
#Description:Compressional Slowness
DTCO = Variable("Becconsall-1Z", "LQC", "DTCO", u"Compressional Slowness", u"us/ft")
parameterDict.update({'DTCO' : Parameter(name='DTCO',bname='Dtco',type='Variable Optional',family='Compressional Slowness',measurement='',unit='us/ft',value='Becconsall-1Z.LQC.DTCO',mode='In',description='Compressional Slowness',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Rd
#Family:Resistivity - Deep
#Unit:ohm.m
#Mode:In
#Description:Deep Resistivity
RD = Variable("Becconsall-1Z", "LQC", "RD", u"Resistivity - Deep", u"ohm.m")
parameterDict.update({'RD' : Parameter(name='RD',bname='Rd',type='Variable',family='Resistivity - Deep',measurement='',unit='ohm.m',value='Becconsall-1Z.LQC.RD',mode='In',description='Deep Resistivity',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Temperature Method
#Group:Wellbore Properties
#List:1. Fix at Start Temperature/2. Variable
Temperature_Method = u"2. Variable"
parameterDict.update({'Temperature_Method' : Parameter(name='Temperature_Method',bname='',type='String',family='',measurement='',unit='',value='2. Variable',mode='In',description='Temperature Method',group='Wellbore Properties',min='',max='',list='1. Fix at Start Temperature/2. Variable',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ft
Start_Depth_Temperature_unit = u"ft"
#Measurement:Depth
Start_Depth_Temperature_measurement = u"Depth"
#Mode:In
#Description:Start Depth for Temperature
#Group:Wellbore Properties
#Minimum:-30
#Maximum:50000
#List:
Start_Depth_Temperature = 4432
parameterDict.update({'Start_Depth_Temperature' : Parameter(name='Start_Depth_Temperature',bname='',type='Number',family='',measurement='Depth',unit='ft',value='4432',mode='In',description='Start Depth for Temperature',group='Wellbore Properties',min='-30',max='50000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:deg C
Start_Temperature_unit = u"deg C"
#Measurement:Temperature
Start_Temperature_measurement = u"Temperature"
#Mode:In
#Description:Start Temperature
#Group:Wellbore Properties
#Minimum:-20
#Maximum:200
#List:
Start_Temperature = 32.00
parameterDict.update({'Start_Temperature' : Parameter(name='Start_Temperature',bname='',type='Number',family='',measurement='Temperature',unit='deg C',value='32.00',mode='In',description='Start Temperature',group='Wellbore Properties',min='-20',max='200',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:degC/ft
Temperature_Gradient_unit = u"degC/ft"
#Measurement:Temperature_Per_Length
Temperature_Gradient_measurement = u"Temperature_Per_Length"
#Mode:In
#Description:Temperature Gradient
#Group:Wellbore Properties
#Minimum:-30
#Maximum:50000
#List:
Temperature_Gradient = 0.006867
parameterDict.update({'Temperature_Gradient' : Parameter(name='Temperature_Gradient',bname='',type='Number',family='',measurement='Temperature_Per_Length',unit='degC/ft',value='0.006867',mode='In',description='Temperature Gradient',group='Wellbore Properties',min='-30',max='50000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Pressure Method
#Group:Wellbore Properties
#List:1. Fix at Start Pressure/2. Variable
Pressure_Method = u"2. Variable"
parameterDict.update({'Pressure_Method' : Parameter(name='Pressure_Method',bname='',type='String',family='',measurement='',unit='',value='2. Variable',mode='In',description='Pressure Method',group='Wellbore Properties',min='',max='',list='1. Fix at Start Pressure/2. Variable',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ft
Start_Depth_Pressure_unit = u"ft"
#Measurement:Depth
Start_Depth_Pressure_measurement = u"Depth"
#Mode:In
#Description:Start Depth for Pressure
#Group:Wellbore Properties
#Minimum:14.7
#Maximum:20000
#List:
Start_Depth_Pressure = 4432
parameterDict.update({'Start_Depth_Pressure' : Parameter(name='Start_Depth_Pressure',bname='',type='Number',family='',measurement='Depth',unit='ft',value='4432',mode='In',description='Start Depth for Pressure',group='Wellbore Properties',min='14.7',max='20000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:psi
Start_Pressure_unit = u"psi"
#Measurement:Pressure
Start_Pressure_measurement = u"Pressure"
#Mode:In
#Description:Start Pressure
#Group:Wellbore Properties
#Minimum:14.7
#Maximum:20000
#List:
Start_Pressure = 1919
parameterDict.update({'Start_Pressure' : Parameter(name='Start_Pressure',bname='',type='Number',family='',measurement='Pressure',unit='psi',value='1919',mode='In',description='Start Pressure',group='Wellbore Properties',min='14.7',max='20000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:psi/ft
Pressure_Gradient_unit = u"psi/ft"
#Measurement:Pressure_Gradient
Pressure_Gradient_measurement = u"Pressure_Gradient"
#Mode:In
#Description:Pressure Gradient
#Group:Wellbore Properties
#Minimum:0.01
#Maximum:1.200
#List:
Pressure_Gradient = 0.433
parameterDict.update({'Pressure_Gradient' : Parameter(name='Pressure_Gradient',bname='',type='Number',family='',measurement='Pressure_Gradient',unit='psi/ft',value='0.433',mode='In',description='Pressure Gradient',group='Wellbore Properties',min='0.01',max='1.200',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:in
BitSize_unit = u"in"
#Measurement:
BitSize_measurement = u""
#Mode:In
#Description:Bit Size
#Group:Wellbore Properties
#Minimum:0
#Maximum:40
#List:
BitSize = 8.5
parameterDict.update({'BitSize' : Parameter(name='BitSize',bname='',type='Number',family='',measurement='',unit='in',value='8.5',mode='In',description='Bit Size',group='Wellbore Properties',min='0',max='40',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Badhole Method
#Group:Wellbore Properties
#List:1. Off/2. On - Caliper Only/3. On - Density Correction Only/4. On - Caliper and Density Correction/5. On - Badhole Assumed
Badhole_Method = u"3. On - Density Correction Only"
parameterDict.update({'Badhole_Method' : Parameter(name='Badhole_Method',bname='',type='String',family='',measurement='',unit='',value='3. On - Density Correction Only',mode='In',description='Badhole Method',group='Wellbore Properties',min='',max='',list='1. Off/2. On - Caliper Only/3. On - Density Correction Only/4. On - Caliper and Density Correction/5. On - Badhole Assumed',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:in
Washout_unit = u"in"
#Measurement:
Washout_measurement = u""
#Mode:In
#Description:Maximum Washout
#Group:Wellbore Properties
#Minimum:0
#Maximum:24
#List:
Washout = 0.20
parameterDict.update({'Washout' : Parameter(name='Washout',bname='',type='Number',family='',measurement='',unit='in',value='0.20',mode='In',description='Maximum Washout',group='Wellbore Properties',min='0',max='24',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cm3
Density_Correction_unit = u"g/cm3"
#Measurement:
Density_Correction_measurement = u""
#Mode:In
#Description:Max Density Correction
#Group:Wellbore Properties
#Minimum:0
#Maximum:1
#List:
Density_Correction = 0.072
parameterDict.update({'Density_Correction' : Parameter(name='Density_Correction',bname='',type='Number',family='',measurement='',unit='g/cm3',value='0.072',mode='In',description='Max Density Correction',group='Wellbore Properties',min='0',max='1',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Action on Bad Hole
#Group:Wellbore Properties
#List:1. Blank out results/2. Continue with calculations
BH_Action = u"2. Continue with calculations"
parameterDict.update({'BH_Action' : Parameter(name='BH_Action',bname='',type='String',family='',measurement='',unit='',value='2. Continue with calculations',mode='In',description='Action on Bad Hole',group='Wellbore Properties',min='',max='',list='1. Blank out results/2. Continue with calculations',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Water Property Method
#Group:Fluid Properties
#List:1. Auto /2. Set Value
Method_Water = u"1. Auto "
parameterDict.update({'Method_Water' : Parameter(name='Method_Water',bname='',type='String',family='',measurement='',unit='',value='1. Auto ',mode='In',description='Water Property Method',group='Fluid Properties',min='',max='',list='1. Auto /2. Set Value',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
Set_Rw_unit = u"ohm.m"
#Measurement:
Set_Rw_measurement = u""
#Mode:In
#Description:Water Resistiivty
#Group:Fluid Properties
#Minimum:0.0001
#Maximum:10000
#List:
Set_Rw = 0.02
parameterDict.update({'Set_Rw' : Parameter(name='Set_Rw',bname='',type='Number',family='',measurement='',unit='ohm.m',value='0.02',mode='In',description='Water Resistiivty',group='Fluid Properties',min='0.0001',max='10000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:degC
Set_Rw_Temperature_unit = u"degC"
#Measurement:
Set_Rw_Temperature_measurement = u""
#Mode:In
#Description:Water Temperature
#Group:Fluid Properties
#Minimum:-20
#Maximum:200
#List:
Set_Rw_Temperature = 109.50
parameterDict.update({'Set_Rw_Temperature' : Parameter(name='Set_Rw_Temperature',bname='',type='Number',family='',measurement='',unit='degC',value='109.50',mode='In',description='Water Temperature',group='Fluid Properties',min='-20',max='200',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
GR_Water_unit = u"API"
#Measurement:
GR_Water_measurement = u""
#Mode:In
#Description:GR of water
#Group:Fluid Properties
#Minimum:0
#Maximum:100
#List:
GR_Water = 40.00
parameterDict.update({'GR_Water' : Parameter(name='GR_Water',bname='',type='Number',family='',measurement='',unit='API',value='40.00',mode='In',description='GR of water',group='Fluid Properties',min='0',max='100',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cm3
DEN_Water_unit = u"g/cm3"
#Measurement:
DEN_Water_measurement = u""
#Mode:In
#Description:Density of water
#Group:Fluid Properties
#Minimum:0.8
#Maximum:1.4
#List:
DEN_Water = 1.000
parameterDict.update({'DEN_Water' : Parameter(name='DEN_Water',bname='',type='Number',family='',measurement='',unit='g/cm3',value='1.000',mode='In',description='Density of water',group='Fluid Properties',min='0.8',max='1.4',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
PHIN_Water_unit = u"frac"
#Measurement:
PHIN_Water_measurement = u""
#Mode:In
#Description:PHIN of water
#Group:Fluid Properties
#Minimum:0.8
#Maximum:1.4
#List:
PHIN_Water = 1.000
parameterDict.update({'PHIN_Water' : Parameter(name='PHIN_Water',bname='',type='Number',family='',measurement='',unit='frac',value='1.000',mode='In',description='PHIN of water',group='Fluid Properties',min='0.8',max='1.4',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
DT_Water_unit = u"us/ft"
#Measurement:
DT_Water_measurement = u""
#Mode:In
#Description:DT of water
#Group:Fluid Properties
#Minimum:140
#Maximum:200
#List:
DT_Water = 186.00
parameterDict.update({'DT_Water' : Parameter(name='DT_Water',bname='',type='Number',family='',measurement='',unit='us/ft',value='186.00',mode='In',description='DT of water',group='Fluid Properties',min='140',max='200',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:Ohmm
RES_Water_unit = u"Ohmm"
#Measurement:
RES_Water_measurement = u""
#Mode:In
#Description:Resistivity of water
#Group:Fluid Properties
#Minimum:0.00001
#Maximum:1000000
#List:
RES_Water = 0.02
parameterDict.update({'RES_Water' : Parameter(name='RES_Water',bname='',type='Number',family='',measurement='',unit='Ohmm',value='0.02',mode='In',description='Resistivity of water',group='Fluid Properties',min='0.00001',max='1000000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Hydrocarbon Property Method
#Group:Fluid Properties
#List:1. Auto/2. Specify Values
Method_Hydrocarbons = u"1. Auto"
parameterDict.update({'Method_Hydrocarbons' : Parameter(name='Method_Hydrocarbons',bname='',type='String',family='',measurement='',unit='',value='1. Auto',mode='In',description='Hydrocarbon Property Method',group='Fluid Properties',min='',max='',list='1. Auto/2. Specify Values',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Gas_Gravity_unit = u"unitless"
#Measurement:
Gas_Gravity_measurement = u""
#Mode:In
#Description:Gas Gravity
#Group:Fluid Properties
#Minimum:0
#Maximum:1
#List:
Gas_Gravity = 0.57
parameterDict.update({'Gas_Gravity' : Parameter(name='Gas_Gravity',bname='',type='Number',family='',measurement='',unit='unitless',value='0.57',mode='In',description='Gas Gravity',group='Fluid Properties',min='0',max='1',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:V/V
Gas_Water_Ratio_unit = u"V/V"
#Measurement:
Gas_Water_Ratio_measurement = u""
#Mode:In
#Description:Gas-Water Ratio
#Group:Fluid Properties
#Minimum:0
#Maximum:10000
#List:
Gas_Water_Ratio = 0.00
parameterDict.update({'Gas_Water_Ratio' : Parameter(name='Gas_Water_Ratio',bname='',type='Number',family='',measurement='',unit='V/V',value='0.00',mode='In',description='Gas-Water Ratio',group='Fluid Properties',min='0',max='10000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Oil_API_unit = u"unitless"
#Measurement:
Oil_API_measurement = u""
#Mode:In
#Description:Oil API
#Group:Fluid Properties
#Minimum:0.1
#Maximum:120
#List:
Oil_API = 60
parameterDict.update({'Oil_API' : Parameter(name='Oil_API',bname='',type='Number',family='',measurement='',unit='unitless',value='60',mode='In',description='Oil API',group='Fluid Properties',min='0.1',max='120',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:scf(60F)/bbl
Gas_Oil_Ratio_unit = u"scf(60F)/bbl"
#Measurement:
Gas_Oil_Ratio_measurement = u""
#Mode:In
#Description:Gas Oil Ratio
#Group:Fluid Properties
#Minimum:0
#Maximum:
#List:
Gas_Oil_Ratio = 0.000
parameterDict.update({'Gas_Oil_Ratio' : Parameter(name='Gas_Oil_Ratio',bname='',type='Number',family='',measurement='',unit='scf(60F)/bbl',value='0.000',mode='In',description='Gas Oil Ratio',group='Fluid Properties',min='0',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cm3
DEN_Hydrocarbon_unit = u"g/cm3"
#Measurement:
DEN_Hydrocarbon_measurement = u""
#Mode:In
#Description:Density of hydrocarbon
#Group:Fluid Properties
#Minimum:0.1
#Maximum:1.5
#List:
DEN_Hydrocarbon = 0.200
parameterDict.update({'DEN_Hydrocarbon' : Parameter(name='DEN_Hydrocarbon',bname='',type='Number',family='',measurement='',unit='g/cm3',value='0.200',mode='In',description='Density of hydrocarbon',group='Fluid Properties',min='0.1',max='1.5',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
PHIN_Hydrocarbon_unit = u"frac"
#Measurement:
PHIN_Hydrocarbon_measurement = u""
#Mode:In
#Description:PHIN of hydrocarbon
#Group:Fluid Properties
#Minimum:0.01
#Maximum:1.200
#List:
PHIN_Hydrocarbon = 0.444
parameterDict.update({'PHIN_Hydrocarbon' : Parameter(name='PHIN_Hydrocarbon',bname='',type='Number',family='',measurement='',unit='frac',value='0.444',mode='In',description='PHIN of hydrocarbon',group='Fluid Properties',min='0.01',max='1.200',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
DT_Hydrocarbon_unit = u"us/ft"
#Measurement:
DT_Hydrocarbon_measurement = u""
#Mode:In
#Description:DT of hydrocarbon
#Group:Fluid Properties
#Minimum:
#Maximum:
#List:
DT_Hydrocarbon = 1400
parameterDict.update({'DT_Hydrocarbon' : Parameter(name='DT_Hydrocarbon',bname='',type='Number',family='',measurement='',unit='us/ft',value='1400',mode='In',description='DT of hydrocarbon',group='Fluid Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:Ohmm
RES_Hydrocarbon_unit = u"Ohmm"
#Measurement:
RES_Hydrocarbon_measurement = u""
#Mode:In
#Description:Resistivity of hydrocarbon
#Group:Fluid Properties
#Minimum:
#Maximum:
#List:
RES_Hydrocarbon = 1E+20
parameterDict.update({'RES_Hydrocarbon' : Parameter(name='RES_Hydrocarbon',bname='',type='Number',family='',measurement='',unit='Ohmm',value='1E+20',mode='In',description='Resistivity of hydrocarbon',group='Fluid Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Method
#Group:Model Properties
#List:1. Alfred and Vernick Model/2. Two Component Model (Density-Neutron-Resistivity)/3. Three Component Model (GR-Density-Neutron-Resistivity)/4. Three Component Model (Density-Neutron-Sonic-Resistivity)
Method = u"1. Alfred and Vernick Model"
parameterDict.update({'Method' : Parameter(name='Method',bname='',type='String',family='',measurement='',unit='',value='1. Alfred and Vernick Model',mode='In',description='Method',group='Model Properties',min='',max='',list='1. Alfred and Vernick Model/2. Two Component Model (Density-Neutron-Resistivity)/3. Three Component Model (GR-Density-Neutron-Resistivity)/4. Three Component Model (Density-Neutron-Sonic-Resistivity)',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Crim_Coefficient_unit = u"unitless"
#Measurement:
Crim_Coefficient_measurement = u""
#Mode:In
#Description:Crim Alpha Coefficient
#Group:Model Properties
#Minimum:
#Maximum:
#List:
Crim_Coefficient = 2.000
parameterDict.update({'Crim_Coefficient' : Parameter(name='Crim_Coefficient',bname='',type='Number',family='',measurement='',unit='unitless',value='2.000',mode='In',description='Crim Alpha Coefficient',group='Model Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Critical_Water_Volume_unit = u"unitless"
#Measurement:
Critical_Water_Volume_measurement = u""
#Mode:In
#Description:Critical Water Volume
#Group:Model Properties
#Minimum:
#Maximum:
#List:
Critical_Water_Volume = 0.000
parameterDict.update({'Critical_Water_Volume' : Parameter(name='Critical_Water_Volume',bname='',type='Number',family='',measurement='',unit='unitless',value='0.000',mode='In',description='Critical Water Volume',group='Model Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Critical_Kerogen_Volume_unit = u"unitless"
#Measurement:
Critical_Kerogen_Volume_measurement = u""
#Mode:In
#Description:Critical Kerogen Volume
#Group:Model Properties
#Minimum:
#Maximum:
#List:
Critical_Kerogen_Volume = 0.0180
parameterDict.update({'Critical_Kerogen_Volume' : Parameter(name='Critical_Kerogen_Volume',bname='',type='Number',family='',measurement='',unit='unitless',value='0.0180',mode='In',description='Critical Kerogen Volume',group='Model Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
Sxoe_unit = u"frac"
#Measurement:
Sxoe_measurement = u""
#Mode:In
#Description:Near Wellbore Invasion Parameter
#Group:Model Properties
#Minimum:
#Maximum:
#List:
Sxoe = 1.000
parameterDict.update({'Sxoe' : Parameter(name='Sxoe',bname='',type='Number',family='',measurement='',unit='frac',value='1.000',mode='In',description='Near Wellbore Invasion Parameter',group='Model Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Name of Component #1
#Group:Component #1 Properties
#List:
Name_Comp_1 = u"Component #1"
parameterDict.update({'Name_Comp_1' : Parameter(name='Name_Comp_1',bname='',type='String',family='',measurement='',unit='',value='Component #1',mode='In',description='Name of Component #1',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
GR_Comp_1_unit = u"API"
#Measurement:
GR_Comp_1_measurement = u""
#Mode:In
#Description:GR of Component #1
#Group:Component #1 Properties
#Minimum:
#Maximum:
#List:
GR_Comp_1 = 18
parameterDict.update({'GR_Comp_1' : Parameter(name='GR_Comp_1',bname='',type='Number',family='',measurement='',unit='API',value='18',mode='In',description='GR of Component #1',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cc
Den_Comp_1_unit = u"g/cc"
#Measurement:
Den_Comp_1_measurement = u""
#Mode:In
#Description:Density of Component
#Group:Component #1 Properties
#Minimum:
#Maximum:
#List:
Den_Comp_1 = 3.00
parameterDict.update({'Den_Comp_1' : Parameter(name='Den_Comp_1',bname='',type='Number',family='',measurement='',unit='g/cc',value='3.00',mode='In',description='Density of Component',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
HI_Comp_1_unit = u"frac"
#Measurement:
HI_Comp_1_measurement = u""
#Mode:In
#Description:HI of Component
#Group:Component #1 Properties
#Minimum:
#Maximum:
#List:
HI_Comp_1 = -0.021
parameterDict.update({'HI_Comp_1' : Parameter(name='HI_Comp_1',bname='',type='Number',family='',measurement='',unit='frac',value='-0.021',mode='In',description='HI of Component',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:FRAC BV
PHI_Comp_1_unit = u"FRAC BV"
#Measurement:
PHI_Comp_1_measurement = u""
#Mode:In
#Description:Porosity of Component
#Group:Component #1 Properties
#Minimum:
#Maximum:
#List:
PHI_Comp_1 = 0.01
parameterDict.update({'PHI_Comp_1' : Parameter(name='PHI_Comp_1',bname='',type='Number',family='',measurement='',unit='FRAC BV',value='0.01',mode='In',description='Porosity of Component',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
DT_Comp_1_unit = u"us/ft"
#Measurement:
DT_Comp_1_measurement = u""
#Mode:In
#Description:Compressional Slowness of Component
#Group:Component #1 Properties
#Minimum:
#Maximum:
#List:
DT_Comp_1 = 53.1
parameterDict.update({'DT_Comp_1' : Parameter(name='DT_Comp_1',bname='',type='Number',family='',measurement='',unit='us/ft',value='53.1',mode='In',description='Compressional Slowness of Component',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
RD_Comp_1_unit = u"ohm.m"
#Measurement:
RD_Comp_1_measurement = u""
#Mode:In
#Description:Resistivity of Component
#Group:Component #1 Properties
#Minimum:
#Maximum:
#List:
RD_Comp_1 = 1374
parameterDict.update({'RD_Comp_1' : Parameter(name='RD_Comp_1',bname='',type='Number',family='',measurement='',unit='ohm.m',value='1374',mode='In',description='Resistivity of Component',group='Component #1 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Name Component 2
#Group:Component #2 Properties
#List:
Name_Comp_2 = u"Component #2"
parameterDict.update({'Name_Comp_2' : Parameter(name='Name_Comp_2',bname='',type='String',family='',measurement='',unit='',value='Component #2',mode='In',description='Name Component 2',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
GR_Comp_2_unit = u"API"
#Measurement:
GR_Comp_2_measurement = u""
#Mode:In
#Description:GR of Component #2
#Group:Component #2 Properties
#Minimum:
#Maximum:
#List:
GR_Comp_2 = 100
parameterDict.update({'GR_Comp_2' : Parameter(name='GR_Comp_2',bname='',type='Number',family='',measurement='',unit='API',value='100',mode='In',description='GR of Component #2',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cc
Den_Comp_2_unit = u"g/cc"
#Measurement:
Den_Comp_2_measurement = u""
#Mode:In
#Description:Density of Component
#Group:Component #2 Properties
#Minimum:
#Maximum:
#List:
Den_Comp_2 = 2.971
parameterDict.update({'Den_Comp_2' : Parameter(name='Den_Comp_2',bname='',type='Number',family='',measurement='',unit='g/cc',value='2.971',mode='In',description='Density of Component',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
HI_Comp_2_unit = u"frac"
#Measurement:
HI_Comp_2_measurement = u""
#Mode:In
#Description:HI of Component
#Group:Component #2 Properties
#Minimum:
#Maximum:
#List:
HI_Comp_2 = 0.164
parameterDict.update({'HI_Comp_2' : Parameter(name='HI_Comp_2',bname='',type='Number',family='',measurement='',unit='frac',value='0.164',mode='In',description='HI of Component',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
PHI_Comp_2_unit = u"frac"
#Measurement:
PHI_Comp_2_measurement = u""
#Mode:In
#Description:Porosity of Component
#Group:Component #2 Properties
#Minimum:
#Maximum:
#List:
PHI_Comp_2 = 0.04
parameterDict.update({'PHI_Comp_2' : Parameter(name='PHI_Comp_2',bname='',type='Number',family='',measurement='',unit='frac',value='0.04',mode='In',description='Porosity of Component',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
DT_Comp_2_unit = u"us/ft"
#Measurement:
DT_Comp_2_measurement = u""
#Mode:In
#Description:Compressional Slowness of Component
#Group:Component #2 Properties
#Minimum:
#Maximum:
#List:
DT_Comp_2 = 90.00
parameterDict.update({'DT_Comp_2' : Parameter(name='DT_Comp_2',bname='',type='Number',family='',measurement='',unit='us/ft',value='90.00',mode='In',description='Compressional Slowness of Component',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
RD_Comp_2_unit = u"ohm.m"
#Measurement:
RD_Comp_2_measurement = u""
#Mode:In
#Description:Resistivity of Component
#Group:Component #2 Properties
#Minimum:
#Maximum:
#List:
RD_Comp_2 = 54
parameterDict.update({'RD_Comp_2' : Parameter(name='RD_Comp_2',bname='',type='Number',family='',measurement='',unit='ohm.m',value='54',mode='In',description='Resistivity of Component',group='Component #2 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Name Component 2
#Group:Component #3 Properties
#List:
Name_Comp_3 = u"Component #3"
parameterDict.update({'Name_Comp_3' : Parameter(name='Name_Comp_3',bname='',type='String',family='',measurement='',unit='',value='Component #3',mode='In',description='Name Component 2',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
GR_Comp_3_unit = u"API"
#Measurement:
GR_Comp_3_measurement = u""
#Mode:In
#Description:GR of Component #2
#Group:Component #3 Properties
#Minimum:
#Maximum:
#List:
GR_Comp_3 = 30.00
parameterDict.update({'GR_Comp_3' : Parameter(name='GR_Comp_3',bname='',type='Number',family='',measurement='',unit='API',value='30.00',mode='In',description='GR of Component #2',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cc
Den_Comp_3_unit = u"g/cc"
#Measurement:
Den_Comp_3_measurement = u""
#Mode:In
#Description:Density of Component
#Group:Component #3 Properties
#Minimum:
#Maximum:
#List:
Den_Comp_3 = 2.720
parameterDict.update({'Den_Comp_3' : Parameter(name='Den_Comp_3',bname='',type='Number',family='',measurement='',unit='g/cc',value='2.720',mode='In',description='Density of Component',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
HI_Comp_3_unit = u"frac"
#Measurement:
HI_Comp_3_measurement = u""
#Mode:In
#Description:HI of Component
#Group:Component #3 Properties
#Minimum:
#Maximum:
#List:
HI_Comp_3 = 0.000
parameterDict.update({'HI_Comp_3' : Parameter(name='HI_Comp_3',bname='',type='Number',family='',measurement='',unit='frac',value='0.000',mode='In',description='HI of Component',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
PHI_Comp_3_unit = u"frac"
#Measurement:
PHI_Comp_3_measurement = u""
#Mode:In
#Description:Porosity of Component
#Group:Component #3 Properties
#Minimum:
#Maximum:
#List:
PHI_Comp_3 = 0.000
parameterDict.update({'PHI_Comp_3' : Parameter(name='PHI_Comp_3',bname='',type='Number',family='',measurement='',unit='frac',value='0.000',mode='In',description='Porosity of Component',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
DT_Comp_3_unit = u"us/ft"
#Measurement:
DT_Comp_3_measurement = u""
#Mode:In
#Description:Compressional Slowness of Component
#Group:Component #3 Properties
#Minimum:
#Maximum:
#List:
DT_Comp_3 = 70.00
parameterDict.update({'DT_Comp_3' : Parameter(name='DT_Comp_3',bname='',type='Number',family='',measurement='',unit='us/ft',value='70.00',mode='In',description='Compressional Slowness of Component',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
RD_Comp_3_unit = u"ohm.m"
#Measurement:
RD_Comp_3_measurement = u""
#Mode:In
#Description:Resistivity of Component
#Group:Component #3 Properties
#Minimum:
#Maximum:
#List:
RD_Comp_3 = 10000
parameterDict.update({'RD_Comp_3' : Parameter(name='RD_Comp_3',bname='',type='Number',family='',measurement='',unit='ohm.m',value='10000',mode='In',description='Resistivity of Component',group='Component #3 Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Ro_unit = u"unitless"
#Measurement:
Ro_measurement = u""
#Mode:In
#Description:Vitrinite Reflectance %
#Group:Kerogen Properties
#Minimum:0.000
#Maximum:12.000
#List:
Ro = 0.900
parameterDict.update({'Ro' : Parameter(name='Ro',bname='',type='Number',family='',measurement='',unit='unitless',value='0.900',mode='In',description='Vitrinite Reflectance %',group='Kerogen Properties',min='0.000',max='12.000',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Use Model
#Group:Kerogen Properties
#List:1. Yes/2. No - Use specifed values for state 1
Use_KPM = u"2. No - Use specifed values for state 1"
parameterDict.update({'Use_KPM' : Parameter(name='Use_KPM',bname='',type='String',family='',measurement='',unit='',value='2. No - Use specifed values for state 1',mode='In',description='Use Model',group='Kerogen Properties',min='',max='',list='1. Yes/2. No - Use specifed values for state 1',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
ST1_Ck_unit = u"unitless"
#Measurement:
ST1_Ck_measurement = u""
#Mode:In
#Description:Carbon Factor
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_Ck = 0.800
parameterDict.update({'ST1_Ck' : Parameter(name='ST1_Ck',bname='',type='Number',family='',measurement='',unit='unitless',value='0.800',mode='In',description='Carbon Factor',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
ST1_GR_unit = u"API"
#Measurement:
ST1_GR_measurement = u""
#Mode:In
#Description:Kerogen Gamma Ray
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_GR = 600
parameterDict.update({'ST1_GR' : Parameter(name='ST1_GR',bname='',type='Number',family='',measurement='',unit='API',value='600',mode='In',description='Kerogen Gamma Ray',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST1_Den_unit = u"frac"
#Measurement:
ST1_Den_measurement = u""
#Mode:In
#Description:Kerogen Density
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_Den = 1.25
parameterDict.update({'ST1_Den' : Parameter(name='ST1_Den',bname='',type='Number',family='',measurement='',unit='frac',value='1.25',mode='In',description='Kerogen Density',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST1_HI_unit = u"frac"
#Measurement:
ST1_HI_measurement = u""
#Mode:In
#Description:Kerogen Hydrogen Index
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_HI = 0.600
parameterDict.update({'ST1_HI' : Parameter(name='ST1_HI',bname='',type='Number',family='',measurement='',unit='frac',value='0.600',mode='In',description='Kerogen Hydrogen Index',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST1_PHI_unit = u"frac"
#Measurement:
ST1_PHI_measurement = u""
#Mode:In
#Description:Kerogen Porosity
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_PHI = 0.350
parameterDict.update({'ST1_PHI' : Parameter(name='ST1_PHI',bname='',type='Number',family='',measurement='',unit='frac',value='0.350',mode='In',description='Kerogen Porosity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
ST1_DT_unit = u"us/ft"
#Measurement:
ST1_DT_measurement = u""
#Mode:In
#Description:Kerogen Compressional Slowness
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_DT = 160.00
parameterDict.update({'ST1_DT' : Parameter(name='ST1_DT',bname='',type='Number',family='',measurement='',unit='us/ft',value='160.00',mode='In',description='Kerogen Compressional Slowness',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
ST1_Res_unit = u"ohm.m"
#Measurement:
ST1_Res_measurement = u""
#Mode:In
#Description:Kerogen Resistivity
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST1_Res = 1E+20
parameterDict.update({'ST1_Res' : Parameter(name='ST1_Res',bname='',type='Number',family='',measurement='',unit='ohm.m',value='1E+20',mode='In',description='Kerogen Resistivity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
ST2_Ck_unit = u"unitless"
#Measurement:
ST2_Ck_measurement = u""
#Mode:In
#Description:Carbon Factor
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_Ck = 0.800
parameterDict.update({'ST2_Ck' : Parameter(name='ST2_Ck',bname='',type='Number',family='',measurement='',unit='unitless',value='0.800',mode='In',description='Carbon Factor',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
ST2_GR_unit = u"API"
#Measurement:
ST2_GR_measurement = u""
#Mode:In
#Description:Kerogen Gamma Ray
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_GR = 600
parameterDict.update({'ST2_GR' : Parameter(name='ST2_GR',bname='',type='Number',family='',measurement='',unit='API',value='600',mode='In',description='Kerogen Gamma Ray',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST2_Den_unit = u"frac"
#Measurement:
ST2_Den_measurement = u""
#Mode:In
#Description:Kerogen Density
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_Den = 1.600
parameterDict.update({'ST2_Den' : Parameter(name='ST2_Den',bname='',type='Number',family='',measurement='',unit='frac',value='1.600',mode='In',description='Kerogen Density',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST2_HI_unit = u"frac"
#Measurement:
ST2_HI_measurement = u""
#Mode:In
#Description:Kerogen Hydrogen Index
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_HI = 0.600
parameterDict.update({'ST2_HI' : Parameter(name='ST2_HI',bname='',type='Number',family='',measurement='',unit='frac',value='0.600',mode='In',description='Kerogen Hydrogen Index',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST2_PHI_unit = u"frac"
#Measurement:
ST2_PHI_measurement = u""
#Mode:In
#Description:Kerogen Porosity
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_PHI = 0.000
parameterDict.update({'ST2_PHI' : Parameter(name='ST2_PHI',bname='',type='Number',family='',measurement='',unit='frac',value='0.000',mode='In',description='Kerogen Porosity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
ST2_DT_unit = u"us/ft"
#Measurement:
ST2_DT_measurement = u""
#Mode:In
#Description:Kerogen Compressional Slowness
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_DT = 160.0
parameterDict.update({'ST2_DT' : Parameter(name='ST2_DT',bname='',type='Number',family='',measurement='',unit='us/ft',value='160.0',mode='In',description='Kerogen Compressional Slowness',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
ST2_Res_unit = u"ohm.m"
#Measurement:
ST2_Res_measurement = u""
#Mode:In
#Description:Kerogen Resistivity
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST2_Res = 1E+20
parameterDict.update({'ST2_Res' : Parameter(name='ST2_Res',bname='',type='Number',family='',measurement='',unit='ohm.m',value='1E+20',mode='In',description='Kerogen Resistivity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
ST3_Ck_unit = u"unitless"
#Measurement:
ST3_Ck_measurement = u""
#Mode:In
#Description:Carbon Factor
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_Ck = 1.000
parameterDict.update({'ST3_Ck' : Parameter(name='ST3_Ck',bname='',type='Number',family='',measurement='',unit='unitless',value='1.000',mode='In',description='Carbon Factor',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:API
ST3_GR_unit = u"API"
#Measurement:
ST3_GR_measurement = u""
#Mode:In
#Description:Kerogen Gamma Ray
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_GR = 600
parameterDict.update({'ST3_GR' : Parameter(name='ST3_GR',bname='',type='Number',family='',measurement='',unit='API',value='600',mode='In',description='Kerogen Gamma Ray',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cm3
ST3_Den_unit = u"g/cm3"
#Measurement:
ST3_Den_measurement = u""
#Mode:In
#Description:Kerogen Density
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_Den = 2.250
parameterDict.update({'ST3_Den' : Parameter(name='ST3_Den',bname='',type='Number',family='',measurement='',unit='g/cm3',value='2.250',mode='In',description='Kerogen Density',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST3_HI_unit = u"frac"
#Measurement:
ST3_HI_measurement = u""
#Mode:In
#Description:Kerogen Hydrogen Index
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_HI = 0.2000
parameterDict.update({'ST3_HI' : Parameter(name='ST3_HI',bname='',type='Number',family='',measurement='',unit='frac',value='0.2000',mode='In',description='Kerogen Hydrogen Index',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
ST3_PHI_unit = u"frac"
#Measurement:
ST3_PHI_measurement = u""
#Mode:In
#Description:Kerogen Porosity
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_PHI = 0.100
parameterDict.update({'ST3_PHI' : Parameter(name='ST3_PHI',bname='',type='Number',family='',measurement='',unit='frac',value='0.100',mode='In',description='Kerogen Porosity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
ST3_ST_unit = u"us/ft"
#Measurement:
ST3_ST_measurement = u""
#Mode:In
#Description:Kerogen Compressional Slowness
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_ST = 200.00
parameterDict.update({'ST3_ST' : Parameter(name='ST3_ST',bname='',type='Number',family='',measurement='',unit='us/ft',value='200.00',mode='In',description='Kerogen Compressional Slowness',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
ST3_Res_unit = u"ohm.m"
#Measurement:
ST3_Res_measurement = u""
#Mode:In
#Description:Kerogen Resistivity
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
ST3_Res = 1E-7
parameterDict.update({'ST3_Res' : Parameter(name='ST3_Res',bname='',type='Number',family='',measurement='',unit='ohm.m',value='1E-7',mode='In',description='Kerogen Resistivity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Transition 1 Ro Value
#Group:Kerogen Properties
#List:
TR1_RoVal = u"1.400"
parameterDict.update({'TR1_RoVal' : Parameter(name='TR1_RoVal',bname='',type='String',family='',measurement='',unit='unitless',value='1.400',mode='In',description='Transition 1 Ro Value',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
TR1_RoSig_unit = u"unitless"
#Measurement:
TR1_RoSig_measurement = u""
#Mode:In
#Description:Transition 1 Ro STD Dev
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
TR1_RoSig = 0.300
parameterDict.update({'TR1_RoSig' : Parameter(name='TR1_RoSig',bname='',type='Number',family='',measurement='',unit='unitless',value='0.300',mode='In',description='Transition 1 Ro STD Dev',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
TR2_RoVal_unit = u"unitless"
#Measurement:
TR2_RoVal_measurement = u""
#Mode:In
#Description:Transition 2 Ro Value
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
TR2_RoVal = 4.200
parameterDict.update({'TR2_RoVal' : Parameter(name='TR2_RoVal',bname='',type='Number',family='',measurement='',unit='unitless',value='4.200',mode='In',description='Transition 2 Ro Value',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
TR2_RoSig_unit = u"unitless"
#Measurement:
TR2_RoSig_measurement = u""
#Mode:In
#Description:Transition 2 Ro STD Dev
#Group:Kerogen Properties
#Minimum:
#Maximum:
#List:
TR2_RoSig = 0.200
parameterDict.update({'TR2_RoSig' : Parameter(name='TR2_RoSig',bname='',type='Number',family='',measurement='',unit='unitless',value='0.200',mode='In',description='Transition 2 Ro STD Dev',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cc
Ads_Density_unit = u"g/cc"
#Measurement:
Ads_Density_measurement = u""
#Mode:In
#Description:Adsorbed gas denstiy
#Group:Adsorbed Gas Properties
#Minimum:
#Maximum:
#List:
Ads_Density = 0.370
parameterDict.update({'Ads_Density' : Parameter(name='Ads_Density',bname='',type='Number',family='',measurement='',unit='g/cc',value='0.370',mode='In',description='Adsorbed gas denstiy',group='Adsorbed Gas Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:frac
Ads_HI_unit = u"frac"
#Measurement:
Ads_HI_measurement = u""
#Mode:In
#Description:Adsorbed gas hydrogen index
#Group:Adsorbed Gas Properties
#Minimum:
#Maximum:
#List:
Ads_HI = 0.827
parameterDict.update({'Ads_HI' : Parameter(name='Ads_HI',bname='',type='Number',family='',measurement='',unit='frac',value='0.827',mode='In',description='Adsorbed gas hydrogen index',group='Adsorbed Gas Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:us/ft
Ads_DT_unit = u"us/ft"
#Measurement:
Ads_DT_measurement = u""
#Mode:In
#Description:Adsorbed gas DTCO
#Group:Adsorbed Gas Properties
#Minimum:
#Maximum:
#List:
Ads_DT = 180.0
parameterDict.update({'Ads_DT' : Parameter(name='Ads_DT',bname='',type='Number',family='',measurement='',unit='us/ft',value='180.0',mode='In',description='Adsorbed gas DTCO',group='Adsorbed Gas Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Adsorption Model
#Group:Adsorbed Gas Properties
#List:1. Fixed RSK Value/2. Variable RSK Value
Adsorrption_Model = u"1. Fixed RSK Value"
parameterDict.update({'Adsorrption_Model' : Parameter(name='Adsorrption_Model',bname='',type='String',family='',measurement='',unit='',value='1. Fixed RSK Value',mode='In',description='Adsorption Model',group='Adsorbed Gas Properties',min='',max='',list='1. Fixed RSK Value/2. Variable RSK Value',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
RSK_In_unit = u"unitless"
#Measurement:
RSK_In_measurement = u""
#Mode:In
#Description:Ratio of adsorbed hydrocarbon to kerogen
#Group:Adsorbed Gas Properties
#Minimum:
#Maximum:
#List:
RSK_In = 0.10
parameterDict.update({'RSK_In' : Parameter(name='RSK_In',bname='',type='Number',family='',measurement='',unit='unitless',value='0.10',mode='In',description='Ratio of adsorbed hydrocarbon to kerogen',group='Adsorbed Gas Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:psi
PK_unit = u"psi"
#Measurement:
PK_measurement = u""
#Mode:In
#Description:Langmuir Pressure
#Group:Adsorbed Gas Properties
#Minimum:
#Maximum:
#List:
PK = 1200
parameterDict.update({'PK' : Parameter(name='PK',bname='',type='Number',family='',measurement='',unit='psi',value='1200',mode='In',description='Langmuir Pressure',group='Adsorbed Gas Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Compute Option
#Group:Output Options
#List:1. Off/2. On
Compute_Option = u"2. On"
parameterDict.update({'Compute_Option' : Parameter(name='Compute_Option',bname='',type='String',family='',measurement='',unit='',value='2. On',mode='In',description='Compute Option',group='Output Options',min='',max='',list='1. Off/2. On',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Output Option
#Group:Output Options
#List:1. Off /2. On
Display_Parameters_Option = u"2. On"
parameterDict.update({'Display_Parameters_Option' : Parameter(name='Display_Parameters_Option',bname='',type='String',family='',measurement='',unit='',value='2. On',mode='In',description='Output Option',group='Output Options',min='',max='',list='1. Off /2. On',enable='True',iscombocheckbox='False',isused='True')})
#Type:String
#Mode:In
#Description:Description
#Group:Output Options
#List:1. No/2. Yes
Display_Progress = u"2. Yes"
parameterDict.update({'Display_Progress' : Parameter(name='Display_Progress',bname='',type='String',family='',measurement='',unit='',value='2. Yes',mode='In',description='Description',group='Output Options',min='',max='',list='1. No/2. Yes',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Phit
#Family:Total Porosity
#Unit:frac
#Mode:Out
#Description:Total Porosity
#Format:auto
#Group:Kerogen Properties
PHIT = Variable("Becconsall-1Z", "LQC", "PHIT", u"Total Porosity", u"frac")
PHIT.setGroupName("ORM")
parameterDict.update({'PHIT' : Parameter(name='PHIT',bname='Phit',type='Variable',family='Total Porosity',measurement='',unit='frac',value='Becconsall-1Z.LQC.PHIT',mode='Out',description='Total Porosity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Phie
#Family:Effective Porosity
#Unit:frac
#Mode:Out
#Description:Effective Porosity
#Format:auto
#Group:Kerogen Properties
PHIE = Variable("Becconsall-1Z", "LQC", "PHIE", u"Effective Porosity", u"frac")
PHIE.setGroupName("ORM")
parameterDict.update({'PHIE' : Parameter(name='PHIE',bname='Phie',type='Variable',family='Effective Porosity',measurement='',unit='frac',value='Becconsall-1Z.LQC.PHIE',mode='Out',description='Effective Porosity',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Cbw
#Family:Clay Bound Water
#Unit:frac
#Mode:Out
#Description:Clay Bound Water
#Format:auto
#Group:Kerogen Properties
CBW = Variable("Becconsall-1Z", "LQC", "CBW", u"Clay Bound Water", u"frac")
CBW.setGroupName("ORM")
parameterDict.update({'CBW' : Parameter(name='CBW',bname='Cbw',type='Variable',family='Clay Bound Water',measurement='',unit='frac',value='Becconsall-1Z.LQC.CBW',mode='Out',description='Clay Bound Water',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Bvw
#Family:Bulk Volume Water
#Unit:frac
#Mode:Out
#Description:Bulk Volume of Water
#Format:auto
#Group:Kerogen Properties
BVW = Variable("Becconsall-1Z", "LQC", "BVW", u"Bulk Volume Water", u"frac")
BVW.setGroupName("ORM")
parameterDict.update({'BVW' : Parameter(name='BVW',bname='Bvw',type='Variable',family='Bulk Volume Water',measurement='',unit='frac',value='Becconsall-1Z.LQC.BVW',mode='Out',description='Bulk Volume of Water',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Hcpv
#Family:Hydrocarbon Volume
#Unit:frac
#Mode:Out
#Description:Hydrocarbon Pore Volume
#Format:auto
#Group:Kerogen Properties
HCPV = Variable("Becconsall-1Z", "LQC", "HCPV", u"Hydrocarbon Volume", u"frac")
HCPV.setGroupName("ORM")
parameterDict.update({'HCPV' : Parameter(name='HCPV',bname='Hcpv',type='Variable',family='Hydrocarbon Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.HCPV',mode='Out',description='Hydrocarbon Pore Volume',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Hads
#Family:Adsorbed Hydrocarbon Pore Volume
#Unit:frac
#Mode:Out
#Description:Adsorbed Hydrocarbon Pore Volume
#Format:auto
#Group:Kerogen Properties
HADS = Variable("Becconsall-1Z", "LQC", "HADS", u"Adsorbed Hydrocarbon Pore Volume", u"frac")
HADS.setGroupName("ORM")
parameterDict.update({'HADS' : Parameter(name='HADS',bname='Hads',type='Variable',family='Adsorbed Hydrocarbon Pore Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.HADS',mode='Out',description='Adsorbed Hydrocarbon Pore Volume',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Hfre
#Family:Free Hydrocarbon Pore Volume
#Unit:frac
#Mode:Out
#Description:Free Hydrocarbon Pore Volume
#Format:auto
#Group:Kerogen Properties
HFRE = Variable("Becconsall-1Z", "LQC", "HFRE", u"Free Hydrocarbon Pore Volume", u"frac")
HFRE.setGroupName("ORM")
parameterDict.update({'HFRE' : Parameter(name='HFRE',bname='Hfre',type='Variable',family='Free Hydrocarbon Pore Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.HFRE',mode='Out',description='Free Hydrocarbon Pore Volume',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Swt
#Family:Water Saturation
#Unit:frac
#Mode:Out
#Description:Total Water Saturation
#Format:auto
#Group:Kerogen Properties
SWT = Variable("Becconsall-1Z", "LQC", "SWT", u"Water Saturation", u"frac")
SWT.setGroupName("ORM")
parameterDict.update({'SWT' : Parameter(name='SWT',bname='Swt',type='Variable',family='Water Saturation',measurement='',unit='frac',value='Becconsall-1Z.LQC.SWT',mode='Out',description='Total Water Saturation',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Swe
#Family:Water Saturation
#Unit:frac
#Mode:Out
#Description:Effective Water Saturation
#Format:auto
#Group:Kerogen Properties
SWE = Variable("Becconsall-1Z", "LQC", "SWE", u"Water Saturation", u"frac")
SWE.setGroupName("ORM")
parameterDict.update({'SWE' : Parameter(name='SWE',bname='Swe',type='Variable',family='Water Saturation',measurement='',unit='frac',value='Becconsall-1Z.LQC.SWE',mode='Out',description='Effective Water Saturation',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Vc1
#Family:Component Volume
#Unit:frac
#Mode:Out
#Description:Volume of Component 1
#Format:auto
#Group:Kerogen Properties
VC1 = Variable("Becconsall-1Z", "LQC", "VC1", u"Component Volume", u"frac")
VC1.setGroupName("ORM")
parameterDict.update({'VC1' : Parameter(name='VC1',bname='Vc1',type='Variable',family='Component Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.VC1',mode='Out',description='Volume of Component 1',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Vc2
#Family:Component Volume
#Unit:frac
#Mode:Out
#Description:Volume of Component 2
#Format:auto
#Group:Kerogen Properties
VC2 = Variable("Becconsall-1Z", "LQC", "VC2", u"Component Volume", u"frac")
VC2.setGroupName("ORM")
parameterDict.update({'VC2' : Parameter(name='VC2',bname='Vc2',type='Variable',family='Component Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.VC2',mode='Out',description='Volume of Component 2',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Vc3
#Family:Component Volume
#Unit:frac
#Mode:Out
#Description:Volume of Component 3
#Format:auto
#Group:Kerogen Properties
VC3 = Variable("Becconsall-1Z", "LQC", "VC3", u"Component Volume", u"frac")
VC3.setGroupName("ORM")
parameterDict.update({'VC3' : Parameter(name='VC3',bname='Vc3',type='Variable',family='Component Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.VC3',mode='Out',description='Volume of Component 3',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Vk
#Family:Component Volume
#Unit:frac
#Mode:Out
#Description:Volume of Kerogen
#Format:auto
#Group:Kerogen Properties
VK = Variable("Becconsall-1Z", "LQC", "VK", u"Component Volume", u"frac")
VK.setGroupName("ORM")
parameterDict.update({'VK' : Parameter(name='VK',bname='Vk',type='Variable',family='Component Volume',measurement='',unit='frac',value='Becconsall-1Z.LQC.VK',mode='Out',description='Volume of Kerogen',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Toc
#Family:TOC
#Unit:wtpercent
#Mode:Out
#Description:Total Organic Carbon
#Format:auto
#Group:Kerogen Properties
TOC = Variable("Becconsall-1Z", "LQC", "TOC", u"TOC", u"wtpercent")
TOC.setGroupName("ORM")
parameterDict.update({'TOC' : Parameter(name='TOC',bname='Toc',type='Variable',family='TOC',measurement='',unit='wtpercent',value='Becconsall-1Z.LQC.TOC',mode='Out',description='Total Organic Carbon',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Qc
#Family:Quality Indicator
#Unit:unitless
#Mode:Out
#Description:Quality Control Index
#Format:auto
#Group:Kerogen Properties
QC = Variable("Becconsall-1Z", "LQC", "QC", u"Quality Indicator", u"unitless")
QC.setGroupName("ORM")
parameterDict.update({'QC' : Parameter(name='QC',bname='Qc',type='Variable',family='Quality Indicator',measurement='',unit='unitless',value='Becconsall-1Z.LQC.QC',mode='Out',description='Quality Control Index',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Bhf
#Family:Bad Hole Flag
#Unit:unitless
#Mode:Out
#Description:Bad Hole Flag
#Format:auto
#Group:Kerogen Properties
BHF = Variable("Becconsall-1Z", "LQC", "BHF", u"Bad Hole Flag", u"unitless")
BHF.setGroupName("ORM")
parameterDict.update({'BHF' : Parameter(name='BHF',bname='Bhf',type='Variable',family='Bad Hole Flag',measurement='',unit='unitless',value='Becconsall-1Z.LQC.BHF',mode='Out',description='Bad Hole Flag',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Ftemp
#Family:Formation Temperature (Model)
#Unit:degC
#Mode:Out
#Description:Formation Temperature
#Format:auto
#Group:Kerogen Properties
FTEMP = Variable("Becconsall-1Z", "LQC", "FTEMP", u"Formation Temperature (Model)", u"degC")
FTEMP.setGroupName("ORM")
parameterDict.update({'FTEMP' : Parameter(name='FTEMP',bname='Ftemp',type='Variable',family='Formation Temperature (Model)',measurement='',unit='degC',value='Becconsall-1Z.LQC.FTEMP',mode='Out',description='Formation Temperature',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Fpres
#Family:Formation Pressure (Model)
#Unit:psi
#Mode:Out
#Description:Formation Pressure
#Format:auto
#Group:Kerogen Properties
FPRES = Variable("Becconsall-1Z", "LQC", "FPRES", u"Formation Pressure (Model)", u"psi")
FPRES.setGroupName("ORM")
parameterDict.update({'FPRES' : Parameter(name='FPRES',bname='Fpres',type='Variable',family='Formation Pressure (Model)',measurement='',unit='psi',value='Becconsall-1Z.LQC.FPRES',mode='Out',description='Formation Pressure',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:Gden
#Family:Grain Density
#Unit:g/cm3
#Mode:Out
#Description:Grain Density
#Format:auto
#Group:Kerogen Properties
GDEN = Variable("Becconsall-1Z", "LQC", "GDEN", u"Grain Density", u"g/cm3")
GDEN.setGroupName("ORM")
parameterDict.update({'GDEN' : Parameter(name='GDEN',bname='Gden',type='Variable',family='Grain Density',measurement='',unit='g/cm3',value='Becconsall-1Z.LQC.GDEN',mode='Out',description='Grain Density',group='Kerogen Properties',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:vADSstp
#Family:
#Unit:cm3/g
#Mode:Out
#Description:Adsorbed gas in place at surface conditions
#Format:auto
GIP_ADS = Variable("well", "dataset", "", u"", u"cm3/g")
GIP_ADS.setGroupName("ORM")
parameterDict.update({'GIP_ADS' : Parameter(name='GIP_ADS',bname='vADSstp',type='Variable',family='',measurement='',unit='cm3/g',value='Becconsall-1Z..GIP_ADS',mode='Out',description='Adsorbed gas in place at surface conditions',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:vFREstp
#Family:
#Unit:cm3/g
#Mode:Out
#Description:Free gas in place at surface conditions
#Format:auto
GIP_FRE = Variable("well", "dataset", "", u"", u"cm3/g")
GIP_FRE.setGroupName("ORM")
parameterDict.update({'GIP_FRE' : Parameter(name='GIP_FRE',bname='vFREstp',type='Variable',family='',measurement='',unit='cm3/g',value='Becconsall-1Z..GIP_FRE',mode='Out',description='Free gas in place at surface conditions',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:GIP
#Family:
#Unit:cm3/g
#Mode:Out
#Description:Total gas in place at surface conditions
#Format:auto
GIP_TOT = Variable("well", "dataset", "", u"", u"cm3/g")
GIP_TOT.setGroupName("ORM")
parameterDict.update({'GIP_TOT' : Parameter(name='GIP_TOT',bname='GIP',type='Variable',family='',measurement='',unit='cm3/g',value='Becconsall-1Z..GIP_TOT',mode='Out',description='Total gas in place at surface conditions',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#DeclarationsEnd
#
# 1.0 IMPORT SUPPORTING PROCEDURES:
#==================================
from Techlog import MissingValue # Defines MissingValue from Techlog
import ORMPIMS_CODE as SC
#
# 2.0 INITIALISATIONS:
#=====================
# 2.1 Initialise Log Inputs:
#===========================
Log_DEPTH=MissingValue
Log_TVD=MissingValue
Log_CALI=MissingValue
Log_GR=MissingValue
Log_RHOB=MissingValue
Log_DRHO=MissingValue
Log_PHIN=MissingValue
Log_DTCO=MissingValue
Log_RD=MissingValue
#
# 2.2 Initialisations:
#=====================
iCount=0
#
# 3.0 START MAIN LOOP & COMPUTATIONS:
#====================================
### Begin Automatic Generation Loop [LOOP]###
loopSize = MD.referenceSize()
loopRange = xrange(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	Depth = MD.value(loopIterator)
	Tvd = TVD.value(loopIterator)
	Cali = CALI.value(loopIterator)
	Gr = GR.value(loopIterator)
	Rhob = RHOB.value(loopIterator)
	Drho = DRHO.value(loopIterator)
	Phin = PHIN.value(loopIterator)
	Dtco = DTCO.value(loopIterator)
	Rd = RD.value(loopIterator)
	Phit = MissingValue
	Phie = MissingValue
	Cbw = MissingValue
	Bvw = MissingValue
	Hcpv = MissingValue
	Hads = MissingValue
	Hfre = MissingValue
	Swt = MissingValue
	Swe = MissingValue
	Vc1 = MissingValue
	Vc2 = MissingValue
	Vc3 = MissingValue
	Vk = MissingValue
	Toc = MissingValue
	Qc = MissingValue
	Bhf = MissingValue
	Ftemp = MissingValue
	Fpres = MissingValue
	Gden = MissingValue
	vADSstp = MissingValue
	vFREstp = MissingValue
	GIP = MissingValue
	### Automatic Generation Loop End ###
#
# 3.1 Initialise Outputs:
#========================
	Log_FTEMP=MissingValue
	Log_FPRES=MissingValue
	Log_PHIT=MissingValue
	Log_PHIE=MissingValue
	Log_CBW=MissingValue
	Log_BVW=MissingValue
	Log_HCPV=MissingValue
	Log_HADS=MissingValue
	Log_HFRE=MissingValue
	Log_SWT=MissingValue
	Log_SWE=MissingValue
	Log_SXOT=MissingValue
	Log_SXOE=MissingValue
	Log_VC1=MissingValue
	Log_VC2=MissingValue
	Log_VC3=MissingValue
	Log_VK=MissingValue
	Log_TOC=MissingValue
	Log_QC=MissingValue
	Log_BHF=MissingValue
	Log_RMFA=MissingValue
	Log_RWA=MissingValue
	Log_GDEN=MissingValue
	Log_HFRE=MissingValue
	Log_HADS=MissingValue
#
# 3.2 Read-in Log Values:
#========================
	Log_DEPTH=Depth
	Log_TVD=Tvd
	Log_CALI=Cali
	Log_GR=Gr
	Log_RHOB=Rhob
	Log_DRHO=Drho
	Log_PHIN=Phin
	Log_DTCO=Dtco
	Log_RD=Rd
#
# 3.3 Compute Formation Temperature & Pressure:
#==============================================
	Log_TVD=SC.fTrueVerticalDepth(Log_DEPTH,Log_TVD) # Establish Depth Reference
	Log_FTEMP=SC.fFormationTemperature(Temperature_Method,Log_TVD,Start_Depth_Temperature,Start_Temperature,Temperature_Gradient) # Calculate Formation Temperature (Deg C)
	Log_FPRES=SC.fFormationPressure(Pressure_Method,Log_TVD,Start_Depth_Pressure,Start_Pressure,Pressure_Gradient) # Calculate Formation Pressure (Psi)
#
# 3.4 Evaluate Borehole Conditions:
#==================================
	Log_BHF=SC.BoreHoleQuality(Log_CALI,Log_DRHO,Badhole_Method,BitSize,Washout,Density_Correction)
#
# 3.5 Compute Formation & Borehole Fluid & Kerogen Properties:
#============================================================
# 3.5.1 Establish Formation Water Properties:
#--------------------------------------------
	Gw=GR_Water
	if(Method_Water=="1. Auto "):
		Rw,Sal,Dw,HIw,DTw=SC.fWaterProperties(Set_Rw,Set_Rw_Temperature,Gas_Water_Ratio,Log_FTEMP,Log_FPRES) # Calculate Formation Water Properties
	else:
		Sal=-999.25
		Dw=DEN_Water
		HIw=PHIN_Water
		DTw=DT_Water
		Rw=RES_Water
#
# 3.5.2 Establish Hydrocarbon Properties (Free Gas):
#---------------------------------------------------
	Gf=0
	Rf=1E+20
	if(Method_Hydrocarbons=="1. Auto"):
		Df,HIf,DTf,D_Oil,HI_Oil,DT_Oil,GOR=SC.fHydrocarbonProperties(Gas_Gravity,Oil_API,Gas_Oil_Ratio,Log_FTEMP,Log_FPRES) # Calculate Formation Hydrocarbon Properties
	else:
		Df=DEN_Hydrocarbon
		HIf=PHIN_Hydrocarbon
		DTf=DT_Hydrocarbon
#
# 3.5.3	Establish Properties of Adsorbed Gas:
#--------------------------------------------
	Ga=0.000 # Gamma Ray of Adsorbed (Sorbed) hydrocarbon (API)
	Ra=1E+20 # Resistivity of Adsorbed (Sorbed) hydrocarbon (Ohm.m)
	Da=Ads_Density # Density of Adsorbed (Sorbed) hydrocarbon (g/cc) - Abrose Paper.
	HIa=Ads_HI # Hydrogden Index of Adsorbed (Sorbed) hydrocarbon (g/cc)
	DTa=Ads_DT # Compressional slowness of Adsorbed (Sorbed) hydrocarons (us/ft)
	if(Adsorrption_Model=="2. Variable RSK Value"):
		RSK=RSK_In*(Log_FPRES/PK)/(1+(Log_FPRES/PK))
	else:
		RSK=RSK_In	
#
# 3.5.4 Establish Kerogen Properties:
#-----------------------------------
	if(Use_KPM=="2. No - Use specifed values for state 1"):
		Ck=ST1_Ck
		Gk=ST1_GR
		Dk=ST1_Den
		PHIk=ST1_PHI
		HIk=ST1_HI
		DTk=ST1_DT
		Rk=(1/ST1_Res)
	else:
		Ck=SC.KPMO(Ro,ST1_Ck,ST2_Ck,ST3_Ck,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Ck Factor (Wgt Carbon/Wt Hydrocarbon.
		Gk=SC.KPMO(Ro,ST1_GR,ST2_GR,ST3_GR,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Gamma Ray (API)
		Dk=SC.KPMO(Ro,ST1_Den,ST2_Den,ST3_Den,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Density (g/cm3)
		PHIk=SC.KPMO(Ro,ST1_PHI,ST2_PHI,ST3_PHI,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Porosity(frac)
		HIk=SC.KPMO(Ro,ST1_HI,ST2_HI,ST3_HI,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Hydrogen Index (frac)
		DTk==SC.KPMO(Ro,ST1_DT,ST2_DT,ST3_DT,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Compressional Slowness (us/ft)
		Rk=1/SC.KPMO(Ro,1/ST1_Res,1/ST2_Res,1/ST3_Res,TR1_RoVal,TR2_RoVal,TR1_RoSig,TR2_RoSig,0) # Kerogen Resistivity(Ohm.m)
#
# 3.5.5 Establish Connectivity Theory Resistivity Model Parameters:
#==================================================================
	Cwv=Critical_Water_Volume
	Ckv=Critical_Kerogen_Volume
	Alpha=Crim_Coefficient
# 
# 3.5.6 Define Process Flags:
#============================
# 	iCompute Flag controls whether calculations at a depth take place or not
	if(Compute_Option=="1. Off"):
		iCompute=0
	else:
		if(Log_BHF==0):
			iCompute=1
		else:
			if(BH_Action=="1. Blank out results"):
				iCompute=0
			else:
				iCompute=1
#	 iDisplay Flag controls whether parameters are displayed or not
	if(Display_Parameters_Option=="1. Off"):
		iDisplay=0
	else:
		iDisplay=1
#
# 4.0 Compute Volumertics:
#=========================
	if((Method=="1. Alfred and Vernick Model") and (iCompute==1)):
		Log_PHIT,Log_PHIE,Log_CBW,Log_BVW,Log_HCPV,Log_HFRE,Log_HADS,Log_SWT,Log_SWE,Log_VC1,Log_VC2,Log_VC3,Log_VK,Log_TOC,Log_QC,Log_GDEN=SC.fAVM(Log_RHOB,Dw,Da,Df,Den_Comp_1,PHI_Comp_1,Ck,Dk,PHIk,RSK)
	if((Method=="2. Two Component Model (Density-Neutron-Resistivity)") and (iCompute==1)):
		Log_PHIT,Log_PHIE,Log_CBW,Log_BVW,Log_HCPV,Log_HFRE,Log_HADS,Log_SWT,Log_SWE,Log_VC1,Log_VC2,Log_VC3,Log_VK,Log_TOC,Log_QC,Log_GDEN=SC.ORM2(Log_RHOB,Log_PHIN,Log_DTCO,Log_RD,Dw,HIw,DTw,Rw,Df,HIf,DTf,Rf,Da,HIa,DTa,Ra,Den_Comp_1,HI_Comp_1,DT_Comp_1,PHI_Comp_1,RD_Comp_1,Den_Comp_2,HI_Comp_2,DT_Comp_2,PHI_Comp_2,RD_Comp_2,Den_Comp_3,HI_Comp_3,DT_Comp_3,PHI_Comp_3,RD_Comp_3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Cwv,Ckv,Alpha,Sxoe)
	if((Method=="3. Three Component Model (GR-Density-Neutron-Resistivity)") and (iCompute==1)):
		Log_PHIT,Log_PHIE,Log_CBW,Log_BVW,Log_HCPV,Log_HFRE,Log_HADS,Log_SWT,Log_SWE,Log_VC1,Log_VC2,Log_VC3,Log_VK,Log_TOC,Log_QC,Log_GDEN=SC.ORM3(Log_GR,Log_RHOB,Log_PHIN,Log_RD,Log_DTCO,Dw,HIw,Gw,Rw,DTw,Df,HIf,Gf,Rf,DTf,Da,HIa,Ga,Ra,DTa,Den_Comp_1,HI_Comp_1,GR_Comp_1,PHI_Comp_1,RD_Comp_1,DT_Comp_1,Den_Comp_2,HI_Comp_2,GR_Comp_2,PHI_Comp_2,RD_Comp_2,DT_Comp_2,Den_Comp_3,HI_Comp_3,GR_Comp_3,PHI_Comp_3,RD_Comp_3,DT_Comp_3,Ck,Dk,HIk,Gk,PHIk,Rk,DTk,RSK,Cwv,Ckv,Alpha,Sxoe)
	if((Method=="4. Three Component Model (Density-Neutron-Sonic-Resistivity)") and (iCompute==1)):
		Log_PHIT,Log_PHIE,Log_CBW,Log_BVW,Log_HCPV,Log_HFRE,Log_HADS,Log_SWT,Log_SWE,Log_VC1,Log_VC2,Log_VC3,Log_VK,Log_TOC,Log_QC,Log_GDEN=SC.ORM4(Log_RHOB,Log_PHIN,Log_DTCO,Log_RD,Dw,HIw,DTw,Rw,Df,HIf,DTf,Rf,Da,HIa,DTa,Ra,Den_Comp_1,HI_Comp_1,DT_Comp_1,PHI_Comp_1,RD_Comp_1,Den_Comp_2,HI_Comp_2,DT_Comp_2,PHI_Comp_2,RD_Comp_2,Den_Comp_3,HI_Comp_3,DT_Comp_3,PHI_Comp_3,RD_Comp_3,Ck,Dk,HIk,DTk,PHIk,Rk,RSK,Cwv,Ckv,Alpha,Sxoe)
#
#
# 3.9 Compute Additional Properties:
#===================================
#
# 3.9.2 iCount:
#==============
	iCount=iCount+1
	if(Display_Progress=="2. Yes"):
		print iCount
		
#
# 4.0 OUTPUT RESULTS:
#====================
	Phit=Log_PHIT
	Phie=Log_PHIE
	Cbw=Log_CBW
	Bvw=Log_BVW
	Hcpv=Log_HCPV
	Hads=Log_HADS
	Hfre=Log_HFRE
	Swt=Log_SWT
	Swe=Log_SWE
	Vc1=Log_VC1
	Vc2=Log_VC2
	Vc3=Log_VC3
	Vk=Log_VK
	Toc=Log_TOC
	Qc=Log_QC
	Bhf=Log_BHF
	Ftemp=Log_FTEMP
	Fpres=Log_FPRES
	Gden=Log_GDEN
	
# 4.1 Compute surface GIP volumes:
#=================================
#
	STPw, STPg = 1.097232904, 0.000728201
	vADSstp, vFREstp, GIP = SC.GIPsurfORM(Log_GDEN, Log_HADS, Log_HFRE, Log_PHIT, Log_SWT, Dw, Df, Da, STPw, STPg)
#
# 5.0 END PROCEDURE:
#===================
	### Begin Automatic Generation EndLoop ###
	PHIT.setValue(loopIterator, Phit)
	PHIE.setValue(loopIterator, Phie)
	CBW.setValue(loopIterator, Cbw)
	BVW.setValue(loopIterator, Bvw)
	HCPV.setValue(loopIterator, Hcpv)
	HADS.setValue(loopIterator, Hads)
	HFRE.setValue(loopIterator, Hfre)
	SWT.setValue(loopIterator, Swt)
	SWE.setValue(loopIterator, Swe)
	VC1.setValue(loopIterator, Vc1)
	VC2.setValue(loopIterator, Vc2)
	VC3.setValue(loopIterator, Vc3)
	VK.setValue(loopIterator, Vk)
	TOC.setValue(loopIterator, Toc)
	QC.setValue(loopIterator, Qc)
	BHF.setValue(loopIterator, Bhf)
	FTEMP.setValue(loopIterator, Ftemp)
	FPRES.setValue(loopIterator, Fpres)
	GDEN.setValue(loopIterator, Gden)
	GIP_ADS.setValue(loopIterator, vADSstp)
	GIP_FRE.setValue(loopIterator, vFREstp)
	GIP_TOT.setValue(loopIterator, GIP)
PHIT.save(True)
PHIE.save(True)
CBW.save(True)
BVW.save(True)
HCPV.save(True)
HADS.save(True)
HFRE.save(True)
SWT.save(True)
SWE.save(True)
VC1.save(True)
VC2.save(True)
VC3.save(True)
VK.save(True)
TOC.save(True)
QC.save(True)
BHF.save(True)
FTEMP.save(True)
FPRES.save(True)
GDEN.save(True)
GIP_ADS.save(True)
GIP_FRE.save(True)
GIP_TOT.save(True)
### Automatic Generation EndLoop End ###
print "End ",iCount
if((Display_Parameters_Option=="2. On") and (iCount>0)):
	print ""
	print "FLUID PROPERTY PARAMETERS"
	print "========================="
	print ""
	print "Temperature = ",Ftemp," Deg C  Pressure = ",Fpres, " psi"
	print ''
	print "Water Properties"
	print "----------------"
	print "Density               = ",Dw," g/cc"
	print "Hydrogen Index        = ",HIw," frac"
	print "Acoustic Slowness     = ",DTw," us/ft"
	print "Salinity              = ",Sal," kppm Rw = ",Rw, " Ohmm"
	print ''
	print "Gas Properties"
	print "----------------"
	print "Density               = ",Df," g/cc"
	print "Hydrogen Index        = ",HIf," frac"
	print "Acoustic Slowness     = ",DTf," us/ft"
	print ''

__doc__ = """ORMPIMS - Organic Rich Mudstone Petrophysical Interpretation Models.

Saved 20th February 2019

Modified by KB 25/06/2020:
- added function for STP volume conversions"""
__author__ = """Tim Pritchard"""
__date__ = """2018-01-05"""
__version__ = """1.0"""
__group__ = """ORM"""
__suffix__ = """_Orm"""
__prefix__ = """"""
__executionGranularity__ = """full"""