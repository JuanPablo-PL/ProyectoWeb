package com.company.login.entity;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Data;

import javax.validation.constraints.NotBlank;

@Entity
@Data
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Admin {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @NotBlank(message = "The name is necessary to continue")
    private String name;

    @NotBlank(message = "The lastname is necessary to continue")
    private String lastname;

    @NotBlank(message = "The email is necessary to continue")
    private String email;

    @NotBlank(message = "The password is necessary to continue")
    private String password;
}
