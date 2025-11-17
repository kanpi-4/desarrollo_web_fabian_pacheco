package com.example.demo.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "aviso_adopcion")
public class AvisoAdopcion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "fecha_ingreso")
    private LocalDateTime fechaIngreso;

    @ManyToOne
    @JoinColumn(name = "comuna_id")
    private Comuna comuna;

    private String sector;
    private String nombre;
    private String email;
    private String celular;

    @Column(columnDefinition = "ENUM('gato','perro')")
    private String tipo;

    private Integer cantidad;
    private Integer edad;

    @Column(columnDefinition = "ENUM('a','m')")
    private String unidadMedida;

    @Column(name = "fecha_entrega")
    private LocalDateTime fechaEntrega;

    @Column(columnDefinition = "TEXT")
    private String descripcion;

    // getters y setters

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public LocalDateTime getFechaIngreso() { return fechaIngreso; }
    public void setFechaIngreso(LocalDateTime fechaIngreso) { this.fechaIngreso = fechaIngreso; }

    public Comuna getComuna() { return comuna; }
    public void setComuna(Comuna comuna) { this.comuna = comuna; }

    public String getSector() { return sector; }
    public void setSector(String sector) { this.sector = sector; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getCelular() { return celular; }
    public void setCelular(String celular) { this.celular = celular; }

    public String getTipo() { return tipo; }
    public void setTipo(String tipo) { this.tipo = tipo; }

    public Integer getCantidad() { return cantidad; }
    public void setCantidad(Integer cantidad) { this.cantidad = cantidad; }

    public Integer getEdad() { return edad; }
    public void setEdad(Integer edad) { this.edad = edad; }

    public String getUnidadMedida() { return unidadMedida; }
    public void setUnidadMedida(String unidadMedida) { this.unidadMedida = unidadMedida; }

    public LocalDateTime getFechaEntrega() { return fechaEntrega; }
    public void setFechaEntrega(LocalDateTime fechaEntrega) { this.fechaEntrega = fechaEntrega; }

    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }
}
