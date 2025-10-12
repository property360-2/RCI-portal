import { Loader2 } from 'lucide-react'
import { cn } from '../../lib/utils'

export const LoadingSpinner = ({ size = 'md', className }) => {
  const sizes = {
    sm: 'w-4 h-4',
    md: 'w-6 h-6',
    lg: 'w-8 h-8',
    xl: 'w-12 h-12',
  }

  return (
    <Loader2 
      className={cn('animate-spin text-primary-600', sizes[size], className)} 
    />
  )
}

export const LoadingOverlay = ({ message = 'Loading...' }) => {
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 flex flex-col items-center gap-4">
        <LoadingSpinner size="xl" />
        <p className="text-gray-700 font-medium">{message}</p>
      </div>
    </div>
  )
}

export const LoadingPage = ({ message = 'Loading...' }) => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <LoadingSpinner size="xl" className="mx-auto mb-4" />
        <p className="text-gray-700 font-medium">{message}</p>
      </div>
    </div>
  )
}

export const LoadingButton = ({ children, loading, ...props }) => {
  return (
    <button disabled={loading} {...props}>
      {loading ? (
        <span className="flex items-center gap-2">
          <LoadingSpinner size="sm" />
          Loading...
        </span>
      ) : (
        children
      )}
    </button>
  )
}