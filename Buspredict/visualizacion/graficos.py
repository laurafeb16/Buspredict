# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime, timedelta

def grafico_tiempos_por_hora(datos_horarios, factores_aplicados=None):
    """
    Gráfico 1: Barras por hora con colores según clima/factores
    """
    plt.figure(figsize=(12, 8))
    
    horas = list(datos_horarios.keys())
    tiempos = list(datos_horarios.values())
    
    # Colores según factores
    colores = []
    for hora in horas:
        if factores_aplicados and factores_aplicados.get(hora, {}).get('lluvia', False):
            colores.append('#1f77b4')  # Azul para lluvia
        elif factores_aplicados and factores_aplicados.get(hora, {}).get('quincena', False):
            colores.append('#ff7f0e')  # Naranja para quincena
        else:
            colores.append('#2ca02c')  # Verde normal
    
    bars = plt.bar(horas, tiempos, color=colores, alpha=0.8)
    
    plt.title('TIEMPOS DE ESPERA POR HORA - FACTORES PANAMEÑOS', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Hora del Día', fontsize=12)
    plt.ylabel('Tiempo de Espera (minutos)', fontsize=12)
    
    # Crear leyenda con patches de colores correctos
    lluvia_patch = mpatches.Patch(color='#1f77b4', alpha=0.8, label='Con Lluvia Tropical')
    quincena_patch = mpatches.Patch(color='#ff7f0e', alpha=0.8, label='Día de Quincena')
    normal_patch = mpatches.Patch(color='#2ca02c', alpha=0.8, label='Día Normal')
    
    plt.legend(handles=[lluvia_patch, quincena_patch, normal_patch])
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    return plt

def grafico_comparacion_buses():
    """
    Gráfico 2: Comparación Diablos Rojos vs Metrobús vs Chiva
    """
    plt.figure(figsize=(10, 6))
    
    tipos = ['Diablos Rojos', 'Metrobús', 'Chiva']
    tiempos_promedio = [25, 12, 18]  # minutos promedio
    confiabilidad = [65, 85, 70]     # porcentaje
    
    x = np.arange(len(tipos))
    width = 0.35
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Gráfico de barras para tiempo
    bars1 = ax1.bar(x - width/2, tiempos_promedio, width, 
                    label='Tiempo Promedio (min)', color=['#d62728', '#2ca02c', '#ff7f0e'])
    
    ax1.set_xlabel('Tipo de Bus')
    ax1.set_ylabel('Tiempo Promedio (minutos)', color='black')
    ax1.set_title('COMPARACIÓN DE BUSES EN PANAMÁ', fontweight='bold', fontsize=14)
    
    # Segundo eje para confiabilidad
    ax2 = ax1.twinx()
    bars2 = ax2.bar(x + width/2, confiabilidad, width, 
                    label='Confiabilidad (%)', color=['#d62728', '#2ca02c', '#ff7f0e'], alpha=0.6)
    ax2.set_ylabel('Confiabilidad (%)', color='blue')
    
    ax1.set_xticks(x)
    ax1.set_xticklabels(tipos)
    
    # Leyendas
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    return plt

def grafico_factores_panama():
    """
    Gráfico 3: Factores únicos panameños (quincena, lluvia, etc.)
    """
    plt.figure(figsize=(12, 8))
    
    # Datos de ejemplo
    dias = ['Día Normal', 'Día 15\n(Quincena)', 'Con Lluvia\nTropical', 'Quincena +\nLluvia']
    tiempos_base = [12, 12, 12, 12]
    incrementos = [0, 7, 12, 19]  # minutos adicionales
    
    # Gráfico de barras apiladas
    plt.bar(dias, tiempos_base, label='Tiempo Base', color='#2ca02c', alpha=0.8)
    plt.bar(dias, incrementos, bottom=tiempos_base, label='Factor Panameño', 
           color=['#808080', '#ff7f0e', '#1f77b4', '#d62728'])
    
    plt.title('IMPACTO DE FACTORES ÚNICOS PANAMEÑOS', 
              fontsize=16, fontweight='bold')
    plt.ylabel('Tiempo Total de Espera (minutos)')
    
    # Agregar valores en las barras
    for i, (base, inc) in enumerate(zip(tiempos_base, incrementos)):
        total = base + inc
        plt.text(i, total + 0.5, f'{total} min', ha='center', fontweight='bold')
        if inc > 0:
            plt.text(i, base + inc/2, f'+{inc}', ha='center', color='white', fontweight='bold')
    
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    return plt

def mostrar_graficos_demo():
    """Muestra los 3 gráficos del demo"""
    
    # Datos simulados para el demo
    datos_horarios = {
        '06:00': 8, '07:00': 15, '08:00': 22, '09:00': 18,
        '12:00': 14, '14:00': 11, '17:00': 25, '19:00': 20, '22:00': 9
    }
    
    factores = {
        '07:00': {'quincena': True}, '08:00': {'lluvia': True}, 
        '17:00': {'quincena': True, 'lluvia': True}
    }
    
    # Gráfico 1
    plt1 = grafico_tiempos_por_hora(datos_horarios, factores)
    plt1.show()
    
    # Gráfico 2  
    plt2 = grafico_comparacion_buses()
    plt2.show()
    
    # Gráfico 3
    plt3 = grafico_factores_panama()
    plt3.show()
    
    print("Gráficos generados exitosamente.")
