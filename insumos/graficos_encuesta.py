import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter
import os

df = pd.read_csv("encuesta-estudiantes.csv")
N = len(df)
os.makedirs("graficos", exist_ok=True)
BLUE = "#1f3b73"; ORANGE = "#e08a1e"

def save(fig, name):
    fig.tight_layout(); fig.savefig(f"graficos/{name}.png", dpi=150, bbox_inches="tight"); plt.close(fig)

# G1: P1 conocimiento del CIE
fig, ax = plt.subplots(figsize=(6,3.5))
vals=[(df["q1_conoce"]==v).sum() for v in [1,2,3,4,5]]
ax.bar([1,2,3,4,5], vals, color=BLUE)
for i,v in enumerate(vals): ax.text(i+1, v+0.5, f"{v}\n{100*v/N:.0f}%", ha="center", fontsize=8)
ax.set_title("P1. Conocimiento del CIE (1=nada, 5=mucho)"); ax.set_ylabel("Respuestas"); ax.set_ylim(0,max(vals)+6)
save(fig,"g1_conocimiento_cie")

# G2: P2 situacion
fig, ax = plt.subplots(figsize=(6,3.8))
lab={"INTERES_NOIDEA":"Me interesa,\nsin idea aún","IDEA":"Tengo una\nidea","MARCHA":"Emprendimiento\nen marcha","NOINTERES":"Sin interés"}
vc=df["q2_situacion"].value_counts()
ax.bar([lab[k] for k in vc.index], vc.values, color=ORANGE)
for i,v in enumerate(vc.values): ax.text(i, v+0.4, f"{v} ({100*v/N:.0f}%)", ha="center", fontsize=8)
ax.set_title("P2. Situación frente al emprendimiento"); ax.set_ylim(0,max(vc.values)+6)
save(fig,"g2_situacion")

# G3: P4 afirmaciones (medias)
fig, ax = plt.subplots(figsize=(7,3.5))
items=["q4_importante","q4_opcion_real","q4_cie_util","q4_participar"]
labels=["Emprendimiento\nimportante","Opción real de\ndesarrollo","CIE es un\nespacio útil","Me gustaría\nparticipar"]
means=[df[i].mean() for i in items]
b=ax.barh(labels, means, color=BLUE); ax.set_xlim(0,5)
for i,v in enumerate(means): ax.text(v+0.05, i, f"{v:.2f}", va="center", fontsize=9)
ax.set_title("P4. Nivel de acuerdo (promedio 1-5)"); ax.invert_yaxis()
save(fig,"g3_afirmaciones")

# G4: P5 razones
fig, ax = plt.subplots(figsize=(7,4))
m5={"DESC":"Desconoce los servicios","ACC":"No sabe cómo acceder","CARR":"Carrera no se relaciona","NOIDEA":"No tiene idea de negocio","TIEMPO":"Falta de tiempo","NOPREP":"No se siente preparado","COMPLEJ":"Procesos complejos","YA":"Ya se ha acercado","OTRO":"Otra"}
c5=Counter()
for r in df["q5_razon"].dropna():
    for t in r.split("|"): c5[t]+=1
items=c5.most_common()
ax.barh([m5[k] for k,_ in items],[v for _,v in items], color=ORANGE)
for i,(k,v) in enumerate(items): ax.text(v+0.4, i, f"{v} ({100*v/N:.0f}%)", va="center", fontsize=8)
ax.set_title("P5. Razón por la que no se ha acercado al CIE"); ax.invert_yaxis(); ax.set_xlim(0,max(c5.values())+10)
save(fig,"g4_razones")

# G5: P6 apoyo
fig, ax = plt.subplots(figsize=(7,4))
m6={"MOD":"Asesoría modelo/plan negocio","TAL":"Talleres creatividad","FIN":"Educación financiera","LEG":"Asesoría legal/tributaria","MEN":"Mentorías empresarios","INV":"Contacto inversionistas","MKT":"Marketing digital/ventas","CONV":"Convocatorias/financiación","NET":"Networking"}
c6=Counter()
for r in df["q6_apoyo"].dropna():
    for t in r.split("|"): c6[t]+=1
items=c6.most_common()
ax.barh([m6[k] for k,_ in items],[v for _,v in items], color=BLUE)
for i,(k,v) in enumerate(items): ax.text(v+0.4, i, f"{v} ({100*v/N:.0f}%)", va="center", fontsize=8)
ax.set_title("P6. Tipo de apoyo deseado del CIE"); ax.invert_yaxis(); ax.set_xlim(0,max(c6.values())+12)
save(fig,"g5_apoyo")

# G6: P7 medio
fig, ax = plt.subplots(figsize=(6,3.5))
m7={"CORREO":"Correo inst.","WA":"WhatsApp","TT":"TikTok","IG":"Instagram","WEB":"Página web","CHARLAS":"Charlas en clases"}
vc=df["q7_medio"].value_counts()
ax.bar([m7[k] for k in vc.index], vc.values, color=ORANGE)
for i,v in enumerate(vc.values): ax.text(i, v+0.4, f"{v}", ha="center", fontsize=8)
ax.set_title("P7. Medio preferido para recibir información"); ax.set_ylim(0,max(vc.values)+6)
plt.xticks(rotation=20, ha="right")
save(fig,"g6_medio")

print("Gráficos generados en carpeta 'graficos':")
for f in sorted(os.listdir("graficos")): print("  -", f)
