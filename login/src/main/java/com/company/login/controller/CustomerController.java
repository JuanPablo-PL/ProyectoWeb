package com.company.login.controller;

import com.company.login.entity.Customer;
import com.company.login.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/customer")
public class CustomerController {

    @Autowired
    private CustomerService customerService;

    @PostMapping("/save")
    public ResponseEntity<Boolean> saveCustomer(@Valid @RequestBody Customer customer) {
        customerService.saveCustomer(customer);
        return ResponseEntity.status(HttpStatus.CREATED).body(Boolean.TRUE);
    }

    @GetMapping("/get/{id}")
    public ResponseEntity<Customer> getCustomerById(@PathVariable Long id) {
        Customer customerId = customerService.getCustomerById(id);
        return ResponseEntity.status(HttpStatus.OK).body(customerId);
    }

    @GetMapping("/get/name/{name}")
    public ResponseEntity<List<Customer>> getCustomerByName(@PathVariable String name) {
        List<Customer> customerNameList = customerService.getCustomerByName(name);
        return ResponseEntity.status(HttpStatus.OK).body(customerNameList);
    }

    @GetMapping("/get/all")
    public ResponseEntity<List<Customer>> getAllCustomer() {
        List<Customer> customerList = customerService.getAllCustomer();
        return ResponseEntity.status(HttpStatus.OK).body(customerList);
    }

    @PutMapping("/update/{id}")
    public ResponseEntity<Customer> updateCustomer(@RequestBody Customer customer) {
        Customer cUpdated = customerService.updateCustomer(customer);
        return new ResponseEntity(cUpdated, HttpStatus.OK);
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Boolean> deleteCustomer(@PathVariable Long id) {
        customerService.deleteCustomerById(id);
        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }
}
