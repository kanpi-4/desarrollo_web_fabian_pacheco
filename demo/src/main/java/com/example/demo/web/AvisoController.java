package com.example.demo.web;

import com.example.demo.dto.AvisoListDTO;
import com.example.demo.entity.AvisoAdopcion;
import com.example.demo.repository.AvisoAdopcionRepository;
import com.example.demo.repository.NotaRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;
import java.util.stream.Collectors;

@Controller
public class AvisoController {

    private final AvisoAdopcionRepository avisoRepo;
    private final NotaRepository notaRepo;

    public AvisoController(AvisoAdopcionRepository avisoRepo, NotaRepository notaRepo) {
        this.avisoRepo = avisoRepo;
        this.notaRepo = notaRepo;
    }

    @GetMapping({"/", "/avisos"})
    public String listarAvisos(Model model) {

    List<AvisoAdopcion> avisos = avisoRepo.findAllByOrderByFechaIngresoDesc();

    List<AvisoListDTO> dtos = avisos.stream().map(a -> {
        Long cnt = notaRepo.countByAvisoId(a.getId());
        Double avg = (cnt == 0) ? null : notaRepo.averageByAvisoId(a.getId());
        return new AvisoListDTO(a, avg, cnt);
    }).collect(Collectors.toList());

    model.addAttribute("avisos", dtos);
    return "avisos";
}

}
