package demo.rest.api.controllers;

import java.util.Collection;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import demo.rest.api.model.dto.ConfigResultDto;
import demo.rest.api.repositories.ConfigRepository;

@RestController
@RequestMapping("/config")
public class ConfigController {

	private final ConfigRepository configRepository;

	@Autowired
	public ConfigController(ConfigRepository configRepository) {
		this.configRepository = configRepository;
	}

	@RequestMapping("/all")
	public Collection<ConfigResultDto> getConfigsNotNullUUIDs() {
		return configRepository.getAllConfigDetails();
	}
}
