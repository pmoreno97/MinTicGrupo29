package proyecto.grupo29.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import proyecto.grupo29.seguridad.Modelos.PermisosRoles;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles, String> {
}
