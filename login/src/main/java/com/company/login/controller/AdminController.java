package com.company.login.controller;

import com.company.login.entity.Admin;
import com.company.login.entity.Customer;
import com.company.login.service.AdminService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/admin")
public class AdminController {

    @Autowired
    private AdminService adminService;

    @PostMapping("/save")
    public ResponseEntity<Boolean> saveAdmin(@Valid @RequestBody Admin admin) {
        adminService.saveAdmin(admin);
        return ResponseEntity.status(HttpStatus.CREATED).body(Boolean.TRUE);
    }

    @GetMapping("/get/{id}")
    public ResponseEntity<Admin> getAdminById(@PathVariable Long id) {
        Admin adminId = adminService.getAdminById(id);
        return ResponseEntity.status(HttpStatus.OK).body(adminId);
    }

    @GetMapping("/get/name/{name}")
    public ResponseEntity<List<Admin>> getAdminByName(@PathVariable String name) {
        List<Admin> adminNameList = adminService.getAdminByName(name);
        return ResponseEntity.status(HttpStatus.OK).body(adminNameList);
    }

    @GetMapping("/get/all")
    public ResponseEntity<List<Admin>> getAllAdmin() {
        List<Admin> adminList = adminService.getAllAdmin();
        return ResponseEntity.status(HttpStatus.OK).body(adminList);
    }

    @PutMapping("/update/{id}")
    public ResponseEntity<Admin> updateAdmin(@RequestBody Admin admin) {
        Admin aUpdated = adminService.updateAdmin(admin);
        return new ResponseEntity(aUpdated, HttpStatus.OK);
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Boolean> deleteAdmin(@PathVariable Long id) {
        adminService.deleteAdminById(id);
        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }
}
