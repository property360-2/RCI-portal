import apiClient from './api'

const authService = {
  /**
   * Register new user
   */
  register: async (userData) => {
    const response = await apiClient.post('/auth/register/', {
      username: userData.username,
      email: userData.email,
      password: userData.password,
      password_confirm: userData.confirmPassword, // Fixed: match backend
      first_name: userData.firstName,
      last_name: userData.lastName,
      role: userData.role || 'student',
    })
    return response.data
  },

  /**
   * Login user - Backend returns { access, refresh, user }
   */
  login: async (username, password) => {
    const response = await apiClient.post('/auth/login/', {
      username,
      password,
    })
    return response.data // { access, refresh, user }
  },

  /**
   * Logout user
   */
  logout: async (refreshToken) => {
    try {
      await apiClient.post('/auth/logout/', {
        refresh_token: refreshToken
      })
    } catch (error) {
      console.error('Logout error:', error)
    }
  },

  /**
   * Refresh access token
   */
  refreshToken: async (refreshToken) => {
    const response = await apiClient.post('/auth/token/refresh/', {
      refresh: refreshToken,
    })
    return response.data
  },

  /**
   * Get current user profile - Fixed endpoint
   */
  getCurrentUser: async () => {
    const response = await apiClient.get('/auth/me/')
    return response.data
  },

  /**
   * Change password
   */
  changePassword: async (oldPassword, newPassword) => {
    const response = await apiClient.post('/auth/change-password/', {
      old_password: oldPassword,
      new_password: newPassword,
      new_password_confirm: newPassword,
    })
    return response.data
  },
}

export default authService