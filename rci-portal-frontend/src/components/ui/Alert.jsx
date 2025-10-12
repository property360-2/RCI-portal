import { CheckCircle, XCircle, AlertCircle, Info, X } from 'lucide-react'
import { cn } from '../../lib/utils'

const Alert = ({ 
  type = 'info', 
  title, 
  message, 
  onClose, 
  className 
}) => {
  const variants = {
    success: {
      bg: 'bg-green-50',
      border: 'border-green-200',
      text: 'text-green-800',
      icon: CheckCircle,
      iconColor: 'text-green-500',
    },
    error: {
      bg: 'bg-red-50',
      border: 'border-red-200',
      text: 'text-red-800',
      icon: XCircle,
      iconColor: 'text-red-500',
    },
    warning: {
      bg: 'bg-yellow-50',
      border: 'border-yellow-200',
      text: 'text-yellow-800',
      icon: AlertCircle,
      iconColor: 'text-yellow-500',
    },
    info: {
      bg: 'bg-blue-50',
      border: 'border-blue-200',
      text: 'text-blue-800',
      icon: Info,
      iconColor: 'text-blue-500',
    },
  }

  const variant = variants[type]
  const Icon = variant.icon

  return (
    <div
      className={cn(
        'p-4 rounded-lg border flex items-start gap-3',
        variant.bg,
        variant.border,
        className
      )}
    >
      <Icon className={cn('w-5 h-5 flex-shrink-0 mt-0.5', variant.iconColor)} />
      
      <div className="flex-1">
        {title && (
          <h4 className={cn('font-semibold mb-1', variant.text)}>
            {title}
          </h4>
        )}
        {message && (
          <p className={cn('text-sm', variant.text)}>
            {message}
          </p>
        )}
      </div>

      {onClose && (
        <button
          onClick={onClose}
          className={cn(
            'flex-shrink-0 p-1 rounded hover:bg-black/5 transition-colors',
            variant.text
          )}
        >
          <X className="w-4 h-4" />
        </button>
      )}
    </div>
  )
}

export default Alert