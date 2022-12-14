package proyecto.grupo29.seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import proyecto.grupo29.seguridad.Modelos.Rol;
import proyecto.grupo29.seguridad.Repositorios.RepositorioRol;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/roles")
public class ControladorRol {
    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("")
    public List<Rol> index(){
        return this.miRepositorioRol.findAll();
    }

    @GetMapping("{id}")
    public Rol show(@PathVariable String id){
        return this.miRepositorioRol.findById(id).orElse(null);
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Rol create(@RequestBody Rol infoRol) {
        return this.miRepositorioRol.save(infoRol);
    }

    @PutMapping("{id}")
    public Rol update(@RequestBody Rol infoRol, @PathVariable String id){
        Rol rolActual = this.miRepositorioRol.findById(id).orElse(null);
        if (rolActual!=null && infoRol!=null){
            rolActual.setNombre(infoRol.getNombre());
            rolActual.setDescripcion(infoRol.getDescripcion());
            return this.miRepositorioRol.save(rolActual);
        } else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Rol rolActual = miRepositorioRol.findById(id).orElse(null);
        if (rolActual!=null){
            this.miRepositorioRol.delete(rolActual);
        }
    }
}
