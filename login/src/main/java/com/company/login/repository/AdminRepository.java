package com.company.login.repository;

import com.company.login.entity.Admin;
import com.company.login.entity.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AdminRepository extends JpaRepository<Admin, Long> {

    @Query(value = "SELECT * FROM Admin WHERE name = ?1", nativeQuery = true)
    public List<Admin> getAdminName(String name);
}
