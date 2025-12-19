# Django Blog Project

A simple blog application built with Django.

## User Authentication System

This project implements a full authentication system using Django’s built-in authentication framework.

### Features
- User registration with email
- Login and logout
- Profile view and update
- Secure password handling using Django’s hashing system
- CSRF protection on all authentication forms

### Authentication Flow
1. Users register via `/register`
2. Users log in via `/login`
3. Authenticated users access `/profile`
4. Users can update their username and email
5. Users log out via `/logout`

### Testing Instructions
- Register a new user using `/register`
- Log out and log back in using `/login`
- Edit profile details on `/profile`
- Attempt to access `/profile` while logged out to confirm redirection
