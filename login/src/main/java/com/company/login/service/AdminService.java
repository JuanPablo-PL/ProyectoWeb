package com.company.login.service;

import com.company.login.entity.Admin;
import com.company.login.entity.Customer;
import com.company.login.exception.CustomerNotFoundException;
import com.company.login.repository.AdminRepository;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class AdminService {

    @Autowired
    private AdminRepository adminRepository;

    @PersistenceContext
    EntityManager entityManager;

    public void saveAdmin(Admin admin) {
        adminRepository.save(admin);
    }

    public Admin getAdminById(Long id) {
        Optional<Admin> adminId = adminRepository.findById(id);
        if (adminId.isPresent()) {
            return adminRepository.getReferenceById(id);
        }
        throw new RuntimeException("The Admin's id didn't found");
    }

    public List<Admin> getAdminByName(String name) {
        return adminRepository.getAdminName("%" + name + "%");
    }

    public List<Admin> getAllAdmin() {
        return adminRepository.findAll();
    }

    public Admin updateAdmin(Admin admin) {
        Optional<Admin> resp = adminRepository.findById(admin.getId());
        if (resp.isPresent()) {
            Admin aConsulted = resp.get();

            aConsulted.setName(admin.getName());
            aConsulted.setLastname(admin.getLastname());
            aConsulted.setEmail(admin.getEmail());
            aConsulted.setPassword(admin.getPassword());

            Admin aSave = adminRepository.save(aConsulted);
            return aSave;
        }
        throw new RuntimeException("Can't update the admin");
    }

    public void deleteAdminById(Long id) {
        Optional<Admin> adminDeleteId = adminRepository.findById(id);
        if (adminDeleteId.isPresent()) {
            adminRepository.deleteById(id);
        }
        throw new RuntimeException("The Admin's id didn't found");
    }

    public Admin adminInfo(Admin admin) {
        String query = "FROM Admin WHERE email = :email";
        List<Admin> list = entityManager.createQuery(query)
                .setParameter("email", admin.getEmail())
                .getResultList();

        if (list.isEmpty()) {
            return null;
        }
        return list.get(0);
    }

    @Transactional
    public List<Admin> getAdmin() {
        String query = "FROM Admin";
        return entityManager.createQuery(query).getResultList();
    }
}
