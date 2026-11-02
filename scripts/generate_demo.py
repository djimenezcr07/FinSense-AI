"""Datos exclusivamente sintéticos; mismos resultados con la misma semilla."""
import csv, random, datetime, pathlib

def generate(path):
    rng=random.Random(42); now=datetime.date.today().replace(day=1); rows=[]
    for back in range(30,0,-1):
        n=now.year*12+now.month-1-back; year,month=n//12,n%12+1
        rows.append([f'{year:04}-{month:02}-05','Salario demostración','ingreso','850000.00','Salario',f'S-{year}{month:02}'])
        for day,desc,cat,base in [(8,'Supermercado','Alimentación',78000),(11,'Alquiler','Vivienda',240000),(18,'Transporte','Transporte',32000),(25,'Cafetería','Alimentación',18000)]:
            amount=base+rng.randrange(-3000,3001)
            if back==3 and desc=='Supermercado': amount=220000
            rows.append([f'{year:04}-{month:02}-{day:02}',desc,'gasto',f'{amount:.2f}',cat,f'{desc[:2]}-{year}{month:02}'])
    with open(path,'w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(['fecha','descripcion','tipo','monto','categoria','referencia']);w.writerows(rows)
    return rows

def validate(rows):
    for row in rows:
        datetime.date.fromisoformat(row[0]); assert row[2] in ('ingreso','gasto') and float(row[3])>0
    return len({r[0][:7] for r in rows})
if __name__=='__main__':
    path=pathlib.Path(__file__).resolve().parents[1]/'FinSense'/'examples'/'demo.csv'
    rows=generate(path);print(f'{len(rows)} movimientos sintéticos, {validate(rows)} meses; semilla 42')
