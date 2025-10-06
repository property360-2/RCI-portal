#!/usr/bin/env python
"""
API Testing Script
Tests all major endpoints of the RCI Academic Portal API
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api'

# ANSI color codes for pretty output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_success(message):
    print(f"{GREEN}✓ {message}{RESET}")

def print_error(message):
    print(f"{RED}✗ {message}{RESET}")

def print_info(message):
    print(f"{BLUE}ℹ {message}{RESET}")

def print_section(message):
    print(f"\n{YELLOW}{'='*60}{RESET}")
    print(f"{YELLOW}{message}{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}\n")

# Global variable to store tokens
tokens = {}

# ========================================
# AUTHENTICATION TESTS
# ========================================

def test_login():
    """Test login endpoint"""
    print_section("Testing Authentication")
    
    url = f"{BASE_URL}/auth/login/"
    data = {
        "username": "admin",
        "password": "password123"
    }
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            tokens['access'] = result['access']
            tokens['refresh'] = result['refresh']
            
            print_success(f"Login successful as {result['user']['username']}")
            print_info(f"Role: {result['user']['role']}")
            print_info(f"Access Token: {tokens['access'][:30]}...")
            return True
        else:
            print_error(f"Login failed: {response.status_code}")
            print_error(response.text)
            return False
    except Exception as e:
        print_error(f"Login error: {e}")
        return False


def test_current_user():
    """Test getting current user info"""
    url = f"{BASE_URL}/auth/me/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            user = response.json()
            print_success(f"Retrieved user info: {user['username']} ({user['role']})")
            return True
        else:
            print_error(f"Failed to get user info: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


def test_token_refresh():
    """Test token refresh"""
    url = f"{BASE_URL}/auth/token/refresh/"
    data = {
        "refresh": tokens['refresh']
    }
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            tokens['access'] = result['access']
            print_success("Token refreshed successfully")
            return True
        else:
            print_error(f"Token refresh failed: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# PROGRAM TESTS
# ========================================

def test_get_programs():
    """Test getting all programs"""
    print_section("Testing Programs API")
    
    url = f"{BASE_URL}/programs/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            programs = response.json()
            count = programs.get('count', len(programs)) if isinstance(programs, dict) else len(programs)
            print_success(f"Retrieved {count} programs")
            
            results = programs.get('results', programs) if isinstance(programs, dict) else programs
            for program in results[:3]:
                print_info(f"  - {program['program_code']}: {program['program_name']}")
            
            return True
        else:
            print_error(f"Failed to get programs: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# STUDENT TESTS
# ========================================

def test_get_students():
    """Test getting all students"""
    print_section("Testing Students API")
    
    url = f"{BASE_URL}/students/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            students = response.json()
            count = students.get('count', len(students)) if isinstance(students, dict) else len(students)
            print_success(f"Retrieved {count} students")
            
            results = students.get('results', students) if isinstance(students, dict) else students
            for student in results[:3]:
                print_info(f"  - {student['student_number']}: {student['user_info']['full_name']}")
            
            return True
        else:
            print_error(f"Failed to get students: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# ENROLLMENT TESTS
# ========================================

def test_get_enrollments():
    """Test getting enrollments"""
    print_section("Testing Enrollments API")
    
    url = f"{BASE_URL}/enrollments/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            enrollments = response.json()
            count = enrollments.get('count', len(enrollments)) if isinstance(enrollments, dict) else len(enrollments)
            print_success(f"Retrieved {count} enrollments")
            return True
        else:
            print_error(f"Failed to get enrollments: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# GRADE TESTS
# ========================================

def test_get_grades():
    """Test getting grades"""
    print_section("Testing Grades API")
    
    url = f"{BASE_URL}/grades/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            grades = response.json()
            count = grades.get('count', len(grades)) if isinstance(grades, dict) else len(grades)
            print_success(f"Retrieved {count} grades")
            
            results = grades.get('results', grades) if isinstance(grades, dict) else grades
            for grade in results[:3]:
                print_info(f"  - {grade['student_number']}: {grade['subject_code']} = {grade['grade']}")
            
            return True
        else:
            print_error(f"Failed to get grades: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# SECTIONS TESTS
# ========================================

def test_get_sections():
    """Test getting sections"""
    print_section("Testing Sections API")
    
    url = f"{BASE_URL}/sections/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            sections = response.json()
            count = sections.get('count', len(sections)) if isinstance(sections, dict) else len(sections)
            print_success(f"Retrieved {count} sections")
            return True
        else:
            print_error(f"Failed to get sections: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# AUDIT LOG TESTS
# ========================================

def test_get_audit_logs():
    """Test getting audit logs"""
    print_section("Testing Audit Logs API")
    
    url = f"{BASE_URL}/audit-logs/"
    headers = {
        "Authorization": f"Bearer {tokens['access']}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            logs = response.json()
            count = logs.get('count', len(logs)) if isinstance(logs, dict) else len(logs)
            print_success(f"Retrieved {count} audit log entries")
            
            results = logs.get('results', logs) if isinstance(logs, dict) else logs
            for log in results[:3]:
                print_info(f"  - {log['action']} on {log['entity']} by {log.get('user_name', 'System')}")
            
            return True
        else:
            print_error(f"Failed to get audit logs: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# PERMISSION TESTS
# ========================================

def test_unauthorized_access():
    """Test that endpoints require authentication"""
    print_section("Testing Authorization")
    
    url = f"{BASE_URL}/students/"
    
    try:
        response = requests.get(url)  # no token
        
        if response.status_code == 401:
            print_success("Unauthorized access properly blocked")
            return True
        else:
            print_error(f"Expected 401, got {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


# ========================================
# MAIN TEST RUNNER
# ========================================

def run_all_tests():
    """Run all API tests"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}RCI Academic Portal - API Testing Suite{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    print_info("Starting API tests...")
    print_info(f"Base URL: {BASE_URL}\n")
    
    tests = [
        ("Login", test_login),
        ("Current User", test_current_user),
        ("Token Refresh", test_token_refresh),
        ("Programs", test_get_programs),
        ("Students", test_get_students),
        ("Enrollments", test_get_enrollments),
        ("Grades", test_get_grades),
        ("Sections", test_get_sections),
        ("Audit Logs", test_get_audit_logs),
        ("Unauthorized Access", test_unauthorized_access),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print_error(f"{test_name} crashed: {e}")
            failed += 1
    
    print_section("Test Results Summary")
    print(f"Total Tests: {passed + failed}")
    print_success(f"Passed: {passed}")
    if failed > 0:
        print_error(f"Failed: {failed}")
    else:
        print_success(f"Failed: {failed}")
    
    print(f"\n{BLUE}{'='*60}{RESET}\n")
    
    if failed == 0:
        print_success("🎉 All tests passed! API is working correctly.")
    else:
        print_error("⚠️  Some tests failed. Please check the errors above.")


if __name__ == "__main__":
    try:
        run_all_tests()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Tests interrupted by user{RESET}")
    except Exception as e:
        print_error(f"Test suite error: {e}")
