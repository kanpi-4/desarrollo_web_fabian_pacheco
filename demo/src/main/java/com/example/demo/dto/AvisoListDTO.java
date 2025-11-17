package com.example.demo.dto;

import com.example.demo.entity.AvisoAdopcion;

public class AvisoListDTO {
    private AvisoAdopcion aviso;
    private Double promedio; // null si no hay
    private Long contador;

    public AvisoListDTO(AvisoAdopcion aviso, Double promedio, Long contador) {
        this.aviso = aviso;
        this.promedio = promedio;
        this.contador = contador;
    }

    public AvisoAdopcion getAviso() { return aviso; }
    public Double getPromedio() { return promedio; }
    public Long getContador() { return contador; }
}

