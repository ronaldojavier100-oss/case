import pandas as pd
from collections import Counter

df = pd.read_csv("encuesta-estudiantes.csv")
N = len(df)

fac = {"ECON":"C. Económicas","HUM":"C. Humanas","ING":"Ingeniería","EDU":"C. Educación","SALUD":"C. Salud"}
prog = {"ADM":"Administración de Empresas","CONT":"Contaduría Pública","HIST":"Historia","AGRO":"Ing. Agroindustrial","LMAT":"Lic. Matemáticas","LEDF":"Lic. Ed. Física","LEE":"Lic. Ed. Especial","NUT":"Nutrición y Dietética"}
q2map = {"INTERES_NOIDEA":"Me interesa, pero no tengo idea","IDEA":"Tengo una idea de negocio","MARCHA":"Tengo emprendimiento en marcha","NOINTERES":"Sin interés actualmente"}
q7map = {"CORREO":"Correo institucional","WA":"WhatsApp","TT":"TikTok","IG":"Instagram","WEB":"Página web institucional","CHARLAS":"Charlas en clases"}
q5map = {"DESC":"Desconoce los servicios","ACC":"No sabe cómo acceder","CARR":"Su carrera no se relaciona","NOIDEA":"No tiene idea de negocio","TIEMPO":"Falta de tiempo","NOPREP":"No se siente preparado","COMPLEJ":"Procesos complejos","YA":"Ya se ha acercado","OTRO":"Otra"}
q6map = {"MOD":"Asesoría modelo/plan de negocio","TAL":"Talleres creatividad/innovación","FIN":"Educación financiera","LEG":"Asesoría legal y tributaria","MEN":"Mentorías con empresarios","INV":"Contacto con inversionistas","MKT":"Marketing digital y ventas","CONV":"Convocatorias y financiación","NET":"Espacios de networking"}

def pct(n): return f"{100*n/N:.1f}%"

print("="*60); print(f"ENCUESTA A ESTUDIANTES/EGRESADOS  —  n = {N}"); print("="*60)

print("\n-- Vínculo --")
for k,v in df["vinculo"].value_counts().items():
    print(f"  {'Estudiante' if k=='EST' else 'Egresado'}: {v} ({pct(v)})")

print("\n-- Facultad --")
for k,v in df["facultad"].value_counts().items():
    print(f"  {fac.get(k,k)}: {v} ({pct(v)})")

print("\n-- Programa --")
for k,v in df["programa"].value_counts().items():
    print(f"  {prog.get(k,k)}: {v} ({pct(v)})")

print("\n-- P1. Conocimiento del CIE (1=nada, 5=mucho) --")
for val in [1,2,3,4,5]:
    c=(df["q1_conoce"]==val).sum(); print(f"  {val}: {c} ({pct(c)})")
print(f"  Promedio: {df['q1_conoce'].mean():.2f}")
bajo=(df['q1_conoce']<=2).sum(); print(f"  Conocimiento BAJO (1-2): {bajo} ({pct(bajo)})")

print("\n-- P2. Situación frente al emprendimiento --")
for k,v in df["q2_situacion"].value_counts().items():
    print(f"  {q2map.get(k,k)}: {v} ({pct(v)})")

print("\n-- P3. ¿Su programa le da herramientas para emprender? (1-5) --")
print(f"  Promedio: {df['q3_herramientas'].mean():.2f}")
bajo3=(df['q3_herramientas']<=2).sum(); print(f"  Bajo (1-2): {bajo3} ({pct(bajo3)})")

print("\n-- P4. Afirmaciones (promedio 1-5) --")
print(f"  Emprendimiento importante p/ mi desarrollo: {df['q4_importante'].mean():.2f}")
print(f"  Emprendimiento = opción real de desarrollo: {df['q4_opcion_real'].mean():.2f}")
print(f"  El CIE parece un espacio útil: {df['q4_cie_util'].mean():.2f}")
print(f"  Me gustaría participar en E&I: {df['q4_participar'].mean():.2f}")

print("\n-- P5. Razón por la que NO se ha acercado (multi) --")
c5=Counter()
for row in df["q5_razon"].dropna():
    for t in row.split("|"): c5[t]+=1
for k,v in c5.most_common():
    print(f"  {q5map.get(k,k)}: {v} ({pct(v)})")

print("\n-- P6. Tipo de apoyo deseado (multi) --")
c6=Counter()
for row in df["q6_apoyo"].dropna():
    for t in row.split("|"): c6[t]+=1
for k,v in c6.most_common():
    print(f"  {q6map.get(k,k)}: {v} ({pct(v)})")

print("\n-- P7. Medio preferido de información --")
for k,v in df["q7_medio"].value_counts().items():
    print(f"  {q7map.get(k,k)}: {v} ({pct(v)})")

print("\n-- CRUCE: conocimiento del CIE segun interes --")
print(df.assign(conoce=df['q1_conoce']).groupby('q2_situacion')['q1_conoce'].mean().round(2).to_string())
