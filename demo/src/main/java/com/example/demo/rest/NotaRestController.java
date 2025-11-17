

package com.example.demo.rest;

import com.example.demo.entity.AvisoAdopcion;
import com.example.demo.entity.Nota;
import com.example.demo.repository.AvisoAdopcionRepository;
import com.example.demo.repository.NotaRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/notas")
public class NotaRestController {

    private final NotaRepository notaRepo;
    private final AvisoAdopcionRepository avisoRepo;

    public NotaRestController(NotaRepository notaRepo, AvisoAdopcionRepository avisoRepo) {
        this.notaRepo = notaRepo;
        this.avisoRepo = avisoRepo;
    }

    @PostMapping("/agregar")
    public ResponseEntity<?> agregarNota(@RequestBody Map<String, Object> body) {
        // validar campos
        if (!body.containsKey("avisoId") || !body.containsKey("nota")) {
            return ResponseEntity.badRequest().body(Map.of("error", "Faltan campos avisoId o nota"));
        }

        Integer avisoId;
        Integer notaVal;
        try {
            avisoId = Integer.parseInt(body.get("avisoId").toString());
            notaVal = Integer.parseInt(body.get("nota").toString());
        } catch (NumberFormatException e) {
            return ResponseEntity.badRequest().body(Map.of("error", "avisoId y nota deben ser numeros"));
        }

        if (notaVal < 1 || notaVal > 7) {
            return ResponseEntity.badRequest().body(Map.of("error", "nota debe estar entre 1 y 7"));
        }

        AvisoAdopcion aviso = avisoRepo.findById(avisoId).orElse(null);
        if (aviso == null) {
            return ResponseEntity.badRequest().body(Map.of("error", "aviso no encontrado"));
        }

        Nota n = new Nota();
        n.setAviso(aviso);
        n.setNota(notaVal);
        notaRepo.save(n);

        Double avg = notaRepo.averageByAvisoId(avisoId);
        Long cnt = notaRepo.countByAvisoId(avisoId);

        return ResponseEntity.ok(Map.of(
                "average", avg,
                "count", cnt
        ));
    }
}
