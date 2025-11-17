package com.example.demo.repository;

import com.example.demo.entity.AvisoAdopcion;
import org.springframework.data.repository.CrudRepository;
import java.util.List;

public interface AvisoAdopcionRepository extends CrudRepository<AvisoAdopcion, Integer> {
    List<AvisoAdopcion> findAllByOrderByFechaIngresoDesc();
}
