package com.company.login.service;

import com.company.login.entity.Customer;
import com.company.login.exception.CustomerNotFoundException;
import com.company.login.repository.CustomerRepository;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class CustomerService {

    @Autowired
    private CustomerRepository customerRepository;

    @PersistenceContext
    EntityManager entityManager;

    public void saveCustomer(Customer customer) {
        customerRepository.save(customer);
    }

    public Customer getCustomerById(Long id) {
        Optional<Customer> customerId = customerRepository.findById(id);
        if (customerId.isPresent()) {
            return customerRepository.getReferenceById(id);
        }
        throw new CustomerNotFoundException();
    }

    public List<Customer> getCustomerByName(String name) {
        return customerRepository.getCustomerName("%" + name + "%");
    }

    public List<Customer> getAllCustomer() {
        return customerRepository.findAll();
    }

    public Customer updateCustomer(Customer customer) {
        Optional<Customer> resp = customerRepository.findById(customer.getId());
        if (resp.isPresent()) {
            Customer cConsulted = resp.get();

            cConsulted.setName(customer.getName());
            cConsulted.setLastname(customer.getLastname());
            cConsulted.setEmail(customer.getEmail());
            cConsulted.setPassword(customer.getPassword());

            Customer cSave = customerRepository.save(cConsulted);
            return cSave;
        }
        throw new RuntimeException("Can't update the customer");
    }

    public void deleteCustomerById(Long id) {
        Optional<Customer> customerDeleteId = customerRepository.findById(id);
        if (customerDeleteId.isPresent()) {
            customerRepository.deleteById(id);
        }
        throw new CustomerNotFoundException();
    }

    public Customer customerInfo(Customer customer) {
        String query = "FROM Customer WHERE email = :email";
        List<Customer> list = entityManager.createQuery(query)
                .setParameter("email", customer.getEmail())
                .getResultList();

        if (list.isEmpty()) {
            return null;
        }
        return list.get(0);
    }

    @Transactional
    public List<Customer> getCustomer() {
        String query = "FROM Customer";
        return entityManager.createQuery(query).getResultList();
    }
}
