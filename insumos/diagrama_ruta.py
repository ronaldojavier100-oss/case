import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow
import os

BLUE="#1f3b73"; ORANGE="#e08a1e"; LIGHT="#eaf0fa"; GRAY="#5b6b8c"
fig, ax = plt.subplots(figsize=(13,6.2)); ax.set_xlim(0,13); ax.set_ylim(0,6.2); ax.axis("off")

ax.text(6.5,5.95,"Ruta Institucional de Emprendimiento — CIE, Universidad del Atlántico",
        ha="center",va="top",fontsize=13,fontweight="bold",color=BLUE)

# Transversal band top
top=FancyBboxPatch((0.3,4.75),12.4,0.55,boxstyle="round,pad=0.02,rounding_size=0.1",
                   fc=ORANGE,ec="none",alpha=0.9)
ax.add_patch(top)
ax.text(6.5,5.02,"T1. DIFUSIÓN Y COMUNICACIÓN  (correo institucional + WhatsApp)",
        ha="center",va="center",fontsize=9.5,fontweight="bold",color="white")

phases=[
 ("F1","Sensibilización","Charlas y talleres,\nferias, cine-foros,\ncampañas de difusión"),
 ("F2","Identificación\ne ideación","Convocatorias,\nrecepción de\nideas, semilleros"),
 ("F3","Diagnóstico y\nclasificación","Nivel de madurez;\nruta personali-\nzada"),
 ("F4","Formación y\npreincubación","Modelo negocio,\nfinanzas, MVP,\nvalidación"),
 ("F5","Incubación y\nfortalecimiento","Mentorías, branding,\ndigital, legal/\ntributaria"),
 ("F6","Aceleración,\nfinanciación y\ntransferencia","Convocatorias,\ncapital, PI,\nspin-off, ecosistema"),
]
n=len(phases); x0=0.35; w=1.92; gap=(12.3-n*w)/(n-1); y=1.7; h=2.6
for i,(tag,title,desc) in enumerate(phases):
    x=x0+i*(w+gap)
    box=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.03,rounding_size=0.12",
                       fc=LIGHT,ec=BLUE,lw=1.6); ax.add_patch(box)
    ax.text(x+w/2,y+h-0.28,tag,ha="center",va="center",fontsize=11,fontweight="bold",color=ORANGE)
    ax.text(x+w/2,y+h-0.95,title,ha="center",va="center",fontsize=9.3,fontweight="bold",color=BLUE)
    ax.text(x+w/2,y+0.72,desc,ha="center",va="center",fontsize=7.6,color=GRAY)
    if i<n-1:
        ax.add_patch(FancyArrow(x+w+0.04,y+h/2,gap-0.12,0,width=0.05,
                     head_width=0.28,head_length=0.14,fc=BLUE,ec=BLUE,length_includes_head=True))

# Transversal band bottom
bot=FancyBboxPatch((0.3,0.85),12.4,0.55,boxstyle="round,pad=0.02,rounding_size=0.1",
                   fc=BLUE,ec="none",alpha=0.92); ax.add_patch(bot)
ax.text(6.5,1.12,"T2. SEGUIMIENTO, INDICADORES Y ARTICULACIÓN CON FACULTADES (docente enlace)",
        ha="center",va="center",fontsize=9.5,fontweight="bold",color="white")

ax.text(6.5,0.4,"Ruta no lineal: cada iniciativa ingresa en la fase correspondiente a su nivel de madurez (definido en F3).",
        ha="center",va="center",fontsize=8.5,style="italic",color=GRAY)

os.makedirs("graficos",exist_ok=True)
fig.savefig("graficos/ruta_emprendimiento.png",dpi=160,bbox_inches="tight")
print("Diagrama guardado: graficos/ruta_emprendimiento.png")
