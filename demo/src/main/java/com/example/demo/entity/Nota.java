package com.example.demo.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "nota")
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "aviso_id")
    private AvisoAdopcion aviso;

    private Integer nota;

    // getters y setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public AvisoAdopcion getAviso() { return aviso; }
    public void setAviso(AvisoAdopcion aviso) { this.aviso = aviso; }
    public Integer getNota() { return nota; }
    public void setNota(Integer nota) { this.nota = nota; }
}
