# !python3
# -*- coding utf-8 -*-
from tkinter import *

root = Tk()
var = StringVar()
menu = OptionMenu(root, var, "Option1", "Option2")

menu["activebackground"] = "#e9f5ae"


menu.pack()
mainloop()

keys = ['activebackground', 'activeforeground', 'anchor', 'background', 'bd', 'bg', 'bitmap',
 'borderwidth', 'cursor', 'direction', 'disabledforeground', 'fg', 'font', 'foreground', 
 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'image', 'indicatoron',
 'justify', 'menu', 'padx', 'pady', 'relief', 'compound', 'state', 'takefocus', 'text', 
 'textvariable', 'underline', 'width', 'wraplength'
]


currency = {
"FJD":2.18835,"DJF":177.720259,"AED":3.67297,"SVC":8.755598,"MZN":61.819663,
"ISK":124.860312,"CHF":0.989635,"HRK":6.7421,"ERN":15.00019,"ALL":110.389808,"TWD":30.994003,
"RWF":922.5,"JMD":136.079933,"HKD":7.84045,"MWK":718.994982,"LVL":0.60489,"SCR":13.764026,
"QAR":3.64175,"EUR":0.910155,"ARS":56.856014,"MXN":19.443196,"STD":21560.79,"RSD":107.020291,
"BBD":2.02015,"DKK":6.79646,"GTQ":7.71955,"COP":3432.5,"TTD":6.77355,"KMF":448.325007,
"ZMW":13.162982,"LTL":2.95274,"SAR":3.75155,"CDF":1666.000199,"KZT":386.649522,"DOP":51.494971,
"SRD":7.458028,"SZL":14.880126,"LSL":14.880436,"HNL":24.69499,"UGX":3674.094926,"MYR":4.181048,
"USD":1,"MKD":55.982501,"YER":250.349817,"XDR":0.730751,"CAD":1.327725,"CLP":722.401389,
"MGA":3750.00012,"IRR":42105.000095,"BGN":1.7793,"AFN":78.23994,"MVR":15.40415,"TND":2.8609,
"NOK":9.0542,"SYP":515.000293,"MRO":357.000346,"MUR":36.350091,"FKP":0.80497,"ZAR":14.873102,
"MMK":1520.250356,"EEK":14.360393,"VND":23203,"XAU":0.000657,"BZD":2.01695,"IMP":0.80481,
"TZS":2298.350501,"INR":70.829012,"THB":30.480322,"XPF":109.000381,"CNY":7.118501,
"UZS":9410.00058,"DZD":120.325013,"MOP":8.080201,"GEL":2.969797,"GIP":0.80503,
"EGP":16.305032,"BAM":1.78155,"XOF":600.512855,"ZWL":322.000001,"SGD":1.378185,
"MAD":9.68375,"AUD":1.476899,"NPR":113.434964,"GGP":0.80481,"ILS":3.514802,"KRW":1195.692944,
"PAB":1.00045,"NAD":14.879745,"RON":4.323698,"CUC":1,"BTC":0.000101,"UYU":36.789664,
"AWG":1.801,"BDT":84.528002,"GYD":208.714975,"PLN":3.99665,"CVE":100.030501,"GHS":5.507402,
"KPW":900.048008,"SLL":9449.99991,"ETB":29.496918,"AOA":369.203966,"BSD":1.00015,
"LKR":181.496357,"MNT":2667.763032,"JPY":107.491973,"PGK":3.40355,"CRC":581.000013,
"NIO":33.620636,"OMR":0.385027,"CZK":23.554997,"TOP":2.328397,"BOB":6.91505,"MDL":17.68505,
"NGN":361.494841,"JEP":0.80481,"KHR":4104.999786,"GBP":0.80465,"AZN":1.704941,"SBD":8.275904,
"SDG":45.138987,"KYD":0.83384,"LAK":8820.000043,"LYD":1.409921,"SOS":580.999636,
"VUV":118.103619,"PKR":156.440119,"KGS":69.8245,"IDR":14076.3,"BYN":2.05755,
"VEF":9.987504,"KWD":0.3038,"WST":2.688964,"PHP":52.124973,"BND":1.350796,
"AMD":476.074957,"ZMK":9001.196617,"NZD":1.59152,"SEK":9.721985,"HUF":305.019897,
"PEN":3.36505,"BMD":1,"KES":103.901556,"XCD":2.70255,"LBP":1507.550325,"ANG":1.76595,
"SHP":1.320901,"HTG":95.671969,"TMT":3.5,"TRY":5.726799,"BWP":10.897982,"BYR":19600,
"IQD":1190,"BRL":4.1788,"BTN":70.898987,"UAH":24.416992,"TJS":9.69565,"CLF":0.026181,
"XAF":597.530262,"GMD":50.395014,"BHD":0.375993,"CUP":26.5,"XAG":0.053854,"PYG":6392.197478,
"LRD":208.349517,"GNF":9235.00052,"BIF":1861,"RUB":63.887991,"JOD":0.708896
}

# rez = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))] 