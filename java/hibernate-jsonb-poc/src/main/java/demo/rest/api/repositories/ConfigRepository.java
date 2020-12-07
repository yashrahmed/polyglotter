package demo.rest.api.repositories;

import java.util.Collection;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import demo.rest.api.model.dao.Config;
import demo.rest.api.model.dto.ConfigResultDto;


public interface ConfigRepository extends CrudRepository<Config, Long> {
	@Query(value = "select id, uuid, code from (\n" +
			"SELECT id, \n" +
			"  jsonb_array_elements(jsonb_strip_nulls(config)) ->>'uuid' as uuid,\n" +
			"  jsonb_array_elements(config) ->> 'code' as code\n" +
			"from test) t2\n" +
			"where uuid != 'null'", nativeQuery = true)
	Collection<ConfigResultDto> getAllConfigDetails();
}
