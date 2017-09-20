
from bottle import *
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

user=0

def WriteGpio(pin,status):
	
	GPIO.setup(pin, GPIO.OUT)

	if status==1:
		GPIO.output(pin, GPIO.HIGH)
	elif status==0:
		GPIO.output(pin,GPIO.LOW)

def WritePWM(pin,duty_cycle,freq,pol):
    GPIO.cleanup()
    PWM.start(pin,duty_cycle,freq,pol)


def ChangeFrequency(pin,freq):
        PWM.set_frequency(pin, freq)

def ChangeDutyCycle(pin,duty_cycle):
        PWM.set_duty_cycle(pin,duty_cycle)        

def StopPWM(pin):
            PWM.stop(pin)

def TurnOffPWM():
    PWM.cleanup()


@route('/activate')
def activate():
    return '''
        <form action="/activate" method="post">

            <span>PIN_GPIO: <input name="Pin_GPIO0" placeholder="P8_7" type="text" />
            Value: <input name="value0" placeholder="0" type="number" /></span>
            <br />  
            PIN_GPIO: <input name="Pin_GPIO1" placeholder="P8_8" type="text" />
            Value: <input name="value1" placeholder="0" type="number" />
            <br />  
            PIN_GPIO: <input name="Pin_GPIO2" placeholder="P8_9" type="text" />
            Value: <input name="value2" placeholder="0"  type="number" />
            <br />  
            PIN_GPIO: <input name="Pin_GPIO3" placeholder="P8_10" type="text" />
            Value: <input name="value3" placeholder="0" type="number" />
            <br />  
            PIN_GPIO: <input name="Pin_GPIO4" placeholder="P8_11" type="text" />
            Value: <input name="value4" placeholder="0" type="number" />
            <br />  
            PIN_GPIO: <input name="Pin_GPIO5" placeholder="P8_12" type="text" />
            Value: <input name="value5" placeholder="0" type="number" />
            <br />  
            PIN_GPIO: <input name="Pin_GPIO6" placeholder="P8_14" type="text" />
            Value: <input name="value6" placeholder="0" type="number" />
            <br />  
            PIN_GPIO: <input name="Pin_GPIO7" placeholder="P8_15" type="text" />
            Value: <input name="value7" placeholder="0" type="number" />
            <br />  <br />  

            <span>PIN_PWM: <input name="Pin_PWM0" placeholder="P9_14" type="text" />
            DutyCycle: <input name="Cycle0" placeholder="0.0 to 100.0" type="number" /></span>
            Frequency: <input name="Freq0" placeholder="0" type="number" /></span> 
            Polarity: <input name="Pol0" placeholder="0 or 1" type="number" /></span> 
            <br />
            <span>PIN_PWM: <input name="Pin_PWM0" placeholder="P9_16" type="text" />
            DutyCycle: <input name="Cycle1" placeholder="0.0 to 100.0" type="number" /></span>
            Frequency: <input name="Freq1" placeholder="0" type="number" /></span> 
            Polarity: <input name="Pol1" placeholder="0 or 1" type="number" /></span> 
            <br />
            <span>PIN_PWM: <input name="Pin_PWM0" placeholder="P8_13" type="text" />
            DutyCycle: <input name="Cycle2" placeholder="0.0 to 100.0" type="number" /></span>
            Frequency: <input name="Freq2" placeholder="0" type="number" /></span> 
            Polarity: <input name="Pol2" placeholder="0 or 1" type="number" /></span> 
            <br />
            <span>PIN_PWM: <input name="Pin_PWM0" placeholder="P8_19" type="text" />
            DutyCycle: <input name="Cycle3" placeholder="0.0 to 100.0" type="number" /></span>
            Frequency: <input name="Freq3" placeholder="0" type="number" /></span> 
            Polarity: <input name="Pol3" placeholder="0 or 1" type="number" /></span> 
            <br />     



            
            <br />  <br />  
            <input value="activate" type="submit" />
        </form>
    '''



@route('/activate', method='POST')
def do_activate():

 names_pins=['Pin_GPIO0','Pin_GPIO1','Pin_GPIO1','Pin_GPIO2','Pin_GPIO3','Pin_GPIO4','Pin_GPIO5','Pin_GPIO6','Pin_GPIO7']
 names_values=['value0','value1','value2','value3','value4','value5','value6','value7']
 names_pwm=['Pin_PWM0','Pin_PWM1','Pin_PWM2','Pin_PWM3']
 names_dutycycle=['Cycle0','Cycle1','Cycle2','Cycle3']
 names_freq=['Freq0','Freq1','Freq2','Freq3']
 names_pol=['Pol0','Pol1','Pol2','Pol3']


 global user
 user+=1

 for a in range(4):
     WritePWM(request.forms.get(str(names_pwm[a])),float(request.forms.get(names_dutycycle[a])),float(request.forms.get(names_freq[a])),int(request.forms.get(names_pol[a])))


 for a in range(8):    
     WriteGpio(str(request.forms.get(names_pins[a])),int(request.forms.get(names_values[a])))
      

 return template('index2',conections=user)


if __name__=='__main__':
	run(host='0.0.0.0',port=8000,debug=True)
