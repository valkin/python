#!/bin/bash

echo "Por favor ingrese su nombre: "
read nom
echo "Bienvenido $nom"

echo "Por favor indique su antiguedad en años: "
read years

vacaciones=$years*12

echo "Sus dias de vacaciones son $vacaciones"
