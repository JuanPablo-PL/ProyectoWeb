package com.company.login.controller;

import com.company.login.entity.Customer;
import com.company.login.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class AuthControllerCustomer {
    @Autowired
    private CustomerService customerService;

    @RequestMapping(value = "api/login/customer", method = RequestMethod.POST)
    public String login(@RequestBody Customer customer) {
        Customer customerLogin = customerService.customerInfo(customer);
        if (customerLogin != null) {
            return "Login";
        }
        return "Fail";
    }

    @RequestMapping(value = "api/registrar/customer", method = RequestMethod.GET)
    public List<Customer> getCustomer(){
        return customerService.getCustomer();
    }
}
