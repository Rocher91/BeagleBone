
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<title>Beagle Bone Black</title>
</head>
<body>

	<header>
		
		<h1>BeagleBone Black Service</h1>
		
		%if conections >1:
			<h5>Hay {{conections}} usuarios conectados</h5>
		%else:
			<h5>Hay {{conections}} usuario conectado</h5>
		%end

	</header>

	<div>
		
		%list_inputs=[]
 	 	%for item in list_GpioStatusin:
     		%list_inputs.append(item)
  		%end

  			%list_outputs=[]
  		%for item in list_GpioStatusout:
     		%list_outputs.append(item)
  		%end

  		%list_pins=[]
  		%for item in list_pinout:
     		%list_pins.append(item)
  		%end

  		%list_adc=[]
  		%for item in list_Adc:
     		%list_adc.append(item)
  		%end
		
		<style>		
			
			header{								
				position:relative;
				text-align: center; 
				font-size:30px;
			}
										
			body{
				background-color:#33BAE6;
			}
											
			.inputs{
				display: inline-block;
				position: relative;
				font-size:20px;
				text-indent: 50px;
				padding-right: 10px;
				top: 50px
			}

			.outputs{
				display: inline-block;
				position: relative;
				font-size:20px;
				text-indent: 30px;
				padding-right: 20px;
				top: 100px
			}

			.adc{
				display: inline-block;
				position: relative;
				font-size:20px;
				text-indent: 20px;
				padding-right: 5px;
				top: 200px
			}

		</style>

		<p class="inputs">Input GPIO{{list_pins[0]}}:  {{list_inputs[0]}}</p>
		<p class="inputs">Input GPIO{{list_pins[1]}}:  {{list_inputs[1]}}</p>
		<p class="inputs">Input GPIO{{list_pins[2]}}:  {{list_inputs[2]}}</p>
		<p class="inputs">Input GPIO {{list_pins[3]}}:  {{list_inputs[3]}}</p>
		<p class="inputs">Input GPIO {{list_pins[4]}}:  {{list_inputs[4]}}</p>
		<p class="inputs">Input GPIO {{list_pins[5]}}:  {{list_inputs[5]}}</p>
		<p class="inputs">Input GPIO {{list_pins[6]}}:  {{list_inputs[6]}}</p>
		<p class="inputs">Input GPIO {{list_pins[7]}}:  {{list_inputs[7]}}</p> 
		<p class="outputs">Output GPIO {{list_pins[8]}}:  {{list_outputs[0]}}</p>
		<p class="outputs">Output GPIO {{list_pins[9]}}:  {{list_outputs[1]}}</p>
		<p class="outputs">Output GPIO {{list_pins[10]}}: {{list_outputs[2]}}</p>
		<p class="outputs">Output GPIO {{list_pins[11]}}:  {{list_outputs[3]}}</p>
		<p class="outputs">Output GPIO {{list_pins[12]}}:  {{list_outputs[4]}}</p>
		<p class="outputs">Output GPIO{{list_pins[13]}}:  {{list_outputs[5]}}</p>
		<p class="outputs">Output GPIO {{list_pins[14]}}:  {{list_outputs[6]}}</p>
		<p class="outputs">Output GPIO {{list_pins[15]}}:  {{list_outputs[7]}}</p>
		<p class="adc">AIN0: {{list_adc[0]}}</p>
		<p class="adc">AIN1: {{list_adc[1]}}</p>	
		<p class="adc">AIN2: {{list_adc[2]}}</p>	
		<p class="adc">AIN3: {{list_adc[3]}}</p>	
		<p class="adc">AIN4: {{list_adc[4]}}</p>	
		<p class="adc">AIN5: {{list_adc[5]}}</p>	
		<p class="adc">AIN6: {{list_adc[6]}}</p>		

	</div>

</body>

</html>