package com.example.calculator.service;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorServiceTest {

    private final CalculatorService calculatorService = new CalculatorService();

    @Test
    public void testAdd() {
        assertEquals(5, calculatorService.add(2, 3));
    }

    @Test
    public void testSubtract() {
        assertEquals(1, calculatorService.subtract(5, 4));
    }

    @Test
    public void testMultiply() {
        assertEquals(6, calculatorService.multiply(2, 3));
    }

    @Test
    public void test_divide_normal_case() {
        assertEquals(2.5, calculatorService.divide(5, 2));
    }


    @Test
    public void test_divide_by_zero() {
        assertThrows(IllegalArgumentException.class, () -> {
            calculatorService.divide(5, 0);
        });
    }


}
