from bottle import *
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

user=0

Gpio_pins=["P8_7","P8_8","P8_9","P8_10","P8_11","P8_12","P8_14",
	  "P8_15","P8_16","P8_17","P8_18","P9_12","P9_15","P9_23","P9_25","P9_27"]
Adc_pins=["P9_39","P9_40","P9_37","P9_38","P9_33","P9_36","P9_35"]
Gpio_status_in=[]
Gpio_status_out=[]



def ReadGpiosInputs(Gpio_pins):

	Gpio_status_inputs=[]

	for a in range(8):

		GPIO.setup(Gpio_pins[a],GPIO.IN)
		Gpio_status_inputs.append(GPIO.input(Gpio_pins[a]))
	
	return Gpio_status_inputs


def ReadGpiosOutputs(Gpio_pins):

	Gpio_status_outputs=[]

	for a in range(8,16):

		GPIO.setup(Gpio_pins[a],GPIO.OUT)
		Gpio_status_outputs.append(GPIO.input(Gpio_pins[a]))
	
	return Gpio_status_outputs


def ReadAdc(adc_pin):
	
	adc_rtat=[]
	ADC.setup()
	adc_rtat.append(ADC.read(adc_pin))
	return adc_rtat



def StatusGpio(var1,var2):
	return "Input GPIO P8_7: "+str(var1[0])+"\n"+"Input GPIO P8_8: "+str(var1[1])+"\n"+"Input GPIO P8_9: "+str(var1[2])+"\n"+"Input GPIO P8_10: "+str(var1[3])+"\n"+"Input GPIO P8_11: "+str(var1[4])+"\n"
		

@route('/status')
def status():
	global Gpio_pins

	Gpio_in=ReadGpiosInputs(Gpio_pins)
	Gpio_out=ReadGpiosOutputs(Gpio_pins)
 	
 	print (str(Gpio_in[:])+"\n")
 	print (str(Gpio_out[:]))
 	

	return StatusGpio(Gpio_in,Gpio_out)


@route('/')
def index():
	global user,Gpio_pins,Gpio_status_in,Gpio_status_out
	adc_rtat=[]

	for a in range(7):
		adc_rtat.append(ReadAdc(Adc_pins[a]))
		
	user+=1	
	Gpio_status_in=ReadGpiosInputs(Gpio_pins)
	Gpio_status_out=ReadGpiosOutputs(Gpio_pins)

	
	return template('index',conections=user,list_pinout=Gpio_pins,list_GpioStatusin=Gpio_status_in,list_GpioStatusout=Gpio_status_out,list_Adc=adc_rtat)

	
if __name__=='__main__':
	run(host='0.0.0.0',port=8000,debug=True)
