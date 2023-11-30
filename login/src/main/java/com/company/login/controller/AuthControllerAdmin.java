package com.company.login.controller;

import com.company.login.entity.Admin;
import com.company.login.entity.Customer;
import com.company.login.service.AdminService;
import com.company.login.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class AuthControllerAdmin {
    @Autowired
    private AdminService adminService;

    @RequestMapping(value = "api/login/admin", method = RequestMethod.POST)
    public String login(@RequestBody Admin admin) {
        Admin adminLogin = adminService.adminInfo(admin);
        if (adminLogin != null) {
            return "Login";
        }
        return "Fail";
    }

    @RequestMapping(value = "api/registrar/admin", method = RequestMethod.GET)
    public List<Admin> getAdmin(){
        return adminService.getAdmin();
    }
}
