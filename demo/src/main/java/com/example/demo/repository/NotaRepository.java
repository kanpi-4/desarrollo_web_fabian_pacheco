package com.example.demo.repository;

import com.example.demo.entity.Nota;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface NotaRepository extends CrudRepository<Nota, Integer> {

    List<Nota> findByAviso_Id(Integer avisoId);

    @Query("SELECT COALESCE(AVG(n.nota), 0) FROM Nota n WHERE n.aviso.id = :avisoId")
    Double averageByAvisoId(Integer avisoId);

    @Query("SELECT COUNT(n) FROM Nota n WHERE n.aviso.id = :avisoId")
    Long countByAvisoId(Integer avisoId);
}
