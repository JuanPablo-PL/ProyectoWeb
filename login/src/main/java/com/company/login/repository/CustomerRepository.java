package com.company.login.repository;

import com.company.login.entity.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {

    @Query(value = "SELECT * FROM Customer WHERE name = ?1", nativeQuery = true)
    public List<Customer> getCustomerName(String name);
}
