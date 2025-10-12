import { useState, useCallback } from 'react'
import apiClient from '../services/api'

/**
 * Custom hook for API calls with loading and error states
 * @returns {Object} { data, loading, error, execute }
 */
const useApi = () => {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const execute = useCallback(async (apiCall) => {
    try {
      setLoading(true)
      setError(null)
      const response = await apiCall()
      setData(response.data)
      return response.data
    } catch (err) {
      const errorMessage = err.response?.data?.detail || err.message || 'An error occurred'
      setError(errorMessage)
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const reset = useCallback(() => {
    setData(null)
    setError(null)
    setLoading(false)
  }, [])

  return { data, loading, error, execute, reset }
}

export default useApi