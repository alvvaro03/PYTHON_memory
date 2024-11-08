---

# 🃏 **El Juego de las Parejas (con emojis!)** 🎉

¿Creías que la consola no podía ser divertida? Piensa de nuevo. Este juego de memoria te desafía a emparejar cartas... bueno, en este caso **emojis** 😎. Perfecto para quienes necesitan un descanso, entrenar su cerebro o simplemente reírse cuando la máquina te aplasta.

---

## 🛠️ **Características**

- **Modo 1v1:** ¿Amigos? ¡No más! Compite contra alguien y demuestra quién tiene mejor memoria.  
- **Modo CPU vs Humano:** Porque a veces jugar solo es más relajante... o frustrante, dependiendo de qué tan lista sea la máquina.  
- **Modo CPU vs CPU:** Mira a las máquinas enfrentarse por la supremacía emoji. (Proximamente... pero, hey, Rome wasn't built in a day).  

---

## ⚙️ **Instrucciones de Instalación**

1. Asegúrate de tener **Python 3.x** instalado.  
   Si no, aquí un link por si no tienes nada mejor que hacer: [Descargar Python](https://www.python.org/downloads/) 🐍.  
2. Descarga este repositorio o copia el archivo de código.
3. Ejecuta el juego en la terminal con:  

```bash
python juego_parejas.py
```

4. ¡Listo para jugar!

---

## 🎮 **Cómo Jugar**

### **1. Configura el tablero**  
   - Elige el número de columnas y filas.  
   - **Pro tip:** No te pases de listo, el número máximo de celdas es 30. Y no me hables de números impares, no vamos por ahí.  

### **2. Modos de Juego**
   - **1v1:** Tú y alguien más. Tomen turnos para encontrar parejas. Pierde el que más se equivoque. O gana el menos despistado.  
   - **Jugador vs CPU:** La máquina nunca olvida... o al menos, casi nunca.  
   - **CPU vs CPU:** Trabajo en progreso (a menos que seas fan de mirar cómo las máquinas se lo pasan bomba).  

### **3. Haz tus jugadas**  
   - Selecciona las coordenadas para revelar las cartas.  
   - Encuentra las parejas y acumula puntos.  
   - Si fallas... bueno, el turno pasa y alguien se ríe de ti.  

---

## 🧠 **Ejemplo de Tablero**  
```
- - - -
- - - -
- - - -
```

¿Recuerdas la ubicación de los emojis? ¡No te equivoques! O verás esto:  
```
😎 😡 - -
👾 - - -
- - - -
```

---

## 🎩 **Detalles Técnicos (para los nerds curiosos)**

1. **Lógica del Tablero:** Usa una mezcla de `random.sample` para asegurar que cada pareja aparece exactamente dos veces.  
2. **Verificación de Parejas:** Coordenadas elegidas se comparan para determinar si hay match 💘.  
3. **CPU con Memoria Limitada:** La máquina "recuerda" dónde están algunas cartas reveladas, pero no todas. No es HAL 9000.  
4. **Sin Interfaz Gráfica:** Todo en consola, porque la nostalgia de los '80s está de moda.

---

## 🤖 **Cosas por Mejorar (Porque el perfeccionismo es un camino largo)**

- Agregar el modo **CPU vs CPU** completo.  
- Hacer que los emojis bailen (mentira, no es posible en consola, o sí...?).  
- Mejorar el diseño del tablero para que sea más claro.  

---

## 💡 **Notas del Desarrollador**

1. **Prohibido llorar** si pierdes contra la CPU.  
2. Este juego no guarda datos, así que nadie sabrá cuántas veces fallaste.  
3. Si encuentras bugs, no son errores... son *features ocultos*.  

---

¡Diviértete jugando y encuentra todas las parejas! 🥳
