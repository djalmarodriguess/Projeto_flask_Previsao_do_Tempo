from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html') 

@app.route('/temperatura', methods= ['POST'])
def temperatura():

    cidade = request.form['cidade']

    api = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=39686e2b35a0cf7ebe4d98da4f429e54')
    #Arquivo em json 
    json_api = api.json()
    #Transformando valor em numerico e informando quais as informações a ser usada do json(main e temp)
    kelvin = float(json_api['main']['temp'])
    #Conversão de kelvin para Celsius
    celsius = round(kelvin - 273.15, 1)
    return render_template('temperatura.html', temp = celsius, cidade= cidade)

if __name__ == '__main__':
    app.run(debug= True)