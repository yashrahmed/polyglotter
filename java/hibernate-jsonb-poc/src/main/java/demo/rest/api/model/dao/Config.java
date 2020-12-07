package demo.rest.api.model.dao;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;
import com.vladmihalcea.hibernate.type.json.JsonBinaryType;

@TypeDef(name = "jsonb", typeClass = JsonBinaryType.class)
@Entity
@Table(name = "test")
public class Config implements Serializable {
	@Id
	private int id;

	@Type(type = "jsonb")
	@Column(name = "config", columnDefinition = "jsonb")
	private List<ConfigDetails> configDetails;

	public Config(int id, List<ConfigDetails> configDetails) {
		this.id = id;
		this.configDetails = configDetails;
	}

	public Config() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public List<ConfigDetails> getConfigDetails() {
		return configDetails;
	}

	public void setConfigDetails(List<ConfigDetails> configDetails) {
		this.configDetails = configDetails;
	}
}
