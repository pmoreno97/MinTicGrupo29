package proyecto.grupo29.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import proyecto.grupo29.seguridad.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}
